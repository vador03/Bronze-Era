using System;
using System.IO;

// Converts the temporary 32-bit BGRA DDS produced by Convert-PngToDds.ps1
// into the single-mip DXT5/BC3 format used by EU5 situation illustrations.
public static class DdsBc3Compressor
{
    public static void Convert(string inputPath, string outputPath)
    {
        byte[] src = File.ReadAllBytes(inputPath);
        if (src.Length < 128 || src[0] != 'D' || src[1] != 'D' || src[2] != 'S' || src[3] != ' ')
            throw new InvalidDataException("Input is not a DDS file.");
        int height = BitConverter.ToInt32(src, 12);
        int width = BitConverter.ToInt32(src, 16);
        if (width % 4 != 0 || height % 4 != 0 || src.Length != 128 + width * height * 4)
            throw new InvalidDataException("Expected an unmipped BGRA DDS with dimensions divisible by four.");

        using (var writer = new BinaryWriter(File.Create(outputPath)))
        {
            writer.Write(new byte[] { (byte)'D', (byte)'D', (byte)'S', (byte)' ' });
            writer.Write((uint)124);
            writer.Write((uint)0x00081007); // caps, height, width, pixel format, linear size
            writer.Write((uint)height);
            writer.Write((uint)width);
            writer.Write((uint)(width * height)); // BC3: one byte per pixel
            writer.Write((uint)0);
            writer.Write((uint)0);
            for (int i = 0; i < 11; i++) writer.Write((uint)0);
            writer.Write((uint)32);
            writer.Write((uint)0x4); // FOURCC
            writer.Write(new byte[] { (byte)'D', (byte)'X', (byte)'T', (byte)'5' });
            for (int i = 0; i < 5; i++) writer.Write((uint)0);
            writer.Write((uint)0x1000); // texture
            for (int i = 0; i < 4; i++) writer.Write((uint)0);

            byte[] b = new byte[16], g = new byte[16], r = new byte[16], a = new byte[16];
            for (int by = 0; by < height; by += 4)
            for (int bx = 0; bx < width; bx += 4)
            {
                int amin = 255, amax = 0, minLum = int.MaxValue, maxLum = -1;
                int minPixel = 0, maxPixel = 0;
                for (int y = 0; y < 4; y++)
                for (int x = 0; x < 4; x++)
                {
                    int i = y * 4 + x;
                    int p = 128 + ((by + y) * width + bx + x) * 4;
                    b[i] = src[p]; g[i] = src[p + 1]; r[i] = src[p + 2]; a[i] = src[p + 3];
                    if (a[i] < amin) amin = a[i];
                    if (a[i] > amax) amax = a[i];
                    int lum = r[i] * 3 + g[i] * 6 + b[i];
                    if (lum < minLum) { minLum = lum; minPixel = i; }
                    if (lum > maxLum) { maxLum = lum; maxPixel = i; }
                }

                writer.Write((byte)amax);
                writer.Write((byte)amin);
                int[] ap = new int[8];
                ap[0] = amax; ap[1] = amin;
                if (amax > amin)
                    for (int j = 2; j < 8; j++) ap[j] = ((8 - j) * amax + (j - 1) * amin) / 7;
                else
                    for (int j = 2; j < 6; j++) ap[j] = ((6 - j) * amax + (j - 1) * amin) / 5;
                if (amax <= amin) { ap[6] = 0; ap[7] = 255; }
                ulong alphaBits = 0;
                for (int i = 0; i < 16; i++)
                {
                    int best = 0, error = int.MaxValue;
                    for (int j = 0; j < 8; j++)
                    {
                        int diff = Math.Abs(a[i] - ap[j]);
                        if (diff < error) { error = diff; best = j; }
                    }
                    alphaBits |= (ulong)best << (3 * i);
                }
                for (int j = 0; j < 6; j++) writer.Write((byte)(alphaBits >> (8 * j)));

                ushort c0 = Pack565(r[maxPixel], g[maxPixel], b[maxPixel]);
                ushort c1 = Pack565(r[minPixel], g[minPixel], b[minPixel]);
                if (c0 < c1) { ushort t = c0; c0 = c1; c1 = t; }
                if (c0 == c1) { if (c0 < ushort.MaxValue) c0++; else c1--; }
                writer.Write(c0);
                writer.Write(c1);
                int[] cr = new int[4], cg = new int[4], cb = new int[4];
                Unpack565(c0, out cr[0], out cg[0], out cb[0]);
                Unpack565(c1, out cr[1], out cg[1], out cb[1]);
                for (int channel = 0; channel < 3; channel++)
                {
                    int[] target = channel == 0 ? cr : channel == 1 ? cg : cb;
                    target[2] = (2 * target[0] + target[1]) / 3;
                    target[3] = (target[0] + 2 * target[1]) / 3;
                }
                uint colorBits = 0;
                for (int i = 0; i < 16; i++)
                {
                    int best = 0, error = int.MaxValue;
                    for (int j = 0; j < 4; j++)
                    {
                        int dr = r[i] - cr[j], dg = g[i] - cg[j], db = b[i] - cb[j];
                        int distance = dr * dr + dg * dg + db * db;
                        if (distance < error) { error = distance; best = j; }
                    }
                    colorBits |= (uint)best << (2 * i);
                }
                writer.Write(colorBits);
            }
        }
    }

    private static ushort Pack565(int r, int g, int b)
    {
        return (ushort)(((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3));
    }

    private static void Unpack565(ushort c, out int r, out int g, out int b)
    {
        r = ((c >> 11) & 31) * 255 / 31;
        g = ((c >> 5) & 63) * 255 / 63;
        b = (c & 31) * 255 / 31;
    }
}
