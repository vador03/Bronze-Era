param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$OutputPath,
    [int]$Width = 1280,
    [int]$Height = 720
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$source = [System.Drawing.Image]::FromFile($InputPath)
$bitmap = [System.Drawing.Bitmap]::new($Width, $Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.DrawImage($source, 0, 0, $Width, $Height)
$graphics.Dispose()
$source.Dispose()

$rawPath = "$OutputPath.raw"
$stream = [System.IO.File]::Create($rawPath)
$writer = [System.IO.BinaryWriter]::new($stream)
try {
    # Legacy uncompressed A8R8G8B8 DDS, supported by DirectX texture loaders.
    $writer.Write([System.Text.Encoding]::ASCII.GetBytes('DDS '))
    $writer.Write([uint32]124)
    $writer.Write([uint32]0x0000100F)
    $writer.Write([uint32]$Height)
    $writer.Write([uint32]$Width)
    $writer.Write([uint32]($Width * 4))
    $writer.Write([uint32]0)
    $writer.Write([uint32]0)
    for ($i = 0; $i -lt 11; $i++) { $writer.Write([uint32]0) }
    $writer.Write([uint32]32)
    $writer.Write([uint32]0x41)
    $writer.Write([uint32]0)
    $writer.Write([uint32]32)
    $writer.Write([uint32]0x00FF0000)
    $writer.Write([uint32]0x0000FF00)
    $writer.Write([uint32]0x000000FF)
    $writer.Write([uint32]4278190080)
    $writer.Write([uint32]0x1000)
    for ($i = 0; $i -lt 4; $i++) { $writer.Write([uint32]0) }

    $rectangle = [System.Drawing.Rectangle]::new(0, 0, $Width, $Height)
    $bits = $bitmap.LockBits($rectangle, [System.Drawing.Imaging.ImageLockMode]::ReadOnly, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    try {
        $row = [byte[]]::new($Width * 4)
        for ($y = 0; $y -lt $Height; $y++) {
            $address = [System.IntPtr]::Add($bits.Scan0, $y * $bits.Stride)
            [System.Runtime.InteropServices.Marshal]::Copy($address, $row, 0, $row.Length)
            $writer.Write($row)
        }
    }
    finally { $bitmap.UnlockBits($bits) }
}
finally {
    $writer.Dispose()
    $bitmap.Dispose()
}

try {
    Add-Type -Path (Join-Path $PSScriptRoot 'DdsBc3Compressor.cs')
    [DdsBc3Compressor]::Convert($rawPath, $OutputPath)
}
finally {
    if (Test-Path -LiteralPath $rawPath) { Remove-Item -LiteralPath $rawPath }
}
