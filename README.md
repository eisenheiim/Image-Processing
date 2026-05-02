# Image Processing Application

A Python-based image processing application that performs various operations on PGM (Portable Graymap) format images.

## Features

- **High-Pass Filter**: Edge detection using 3x3 kernel convolution
- **Misalign**: Swap pixels in odd columns vertically
- **Sort Columns**: Sort pixel values in each column independently
- **Sort Rows Border**: Sort pixel values between black (0) pixel borders in each row

## Requirements

- Python 3.6+
- Input images in PGM format

## Usage

```bash
python main.py <input_file> <operation> <output_file>
```

### Examples

```bash
python main.py animals.pgm highpass animals_highpass.pgm
python main.py animals.pgm misalign animals_misalign.pgm
python main.py animals.pgm sort_columns animals_sort_columns.pgm
python main.py animals.pgm sort_rows_border animals_sort_rows_border.pgm
```

## Operations

| Operation | Description |
|-----------|-------------|
| `highpass` | Applies high-pass filter for edge detection |
| `misalign` | Vertically swaps pixels in odd-numbered columns |
| `sort_columns` | Sorts pixel values within each column |
| `sort_rows_border` | Sorts pixel segments between black pixel borders |

## Implementation

### Key Functions

- `read_imagefile()`: Reads PGM image and returns pixel matrix
- `write_imagefile()`: Writes processed image to PGM file
- `convolution()`: Applies kernel-based convolution filter
- `misalign()`: Swaps pixels vertically in odd columns
- `sort_columns()`: Sorts columns independently
- `sort_rows_border()`: Sorts row segments between borders

### Supported Format

**PGM Format Structure:**
```
P2 (or P5)
width height
max_pixel_value
pixel_data...
```

## File Structure

```
Image-Processing/
├── main.py              # Main application
├── Description.pdf      # Detailed specification
├── animals.pgm          # Sample input image
└── animals_*.pgm        # Output examples
```

## Technical Details

- **Convolution Kernel**: 3x3 high-pass filter for edge detection
- **Pixel Range**: 0-255 (clamped automatically)
- **Padding**: Zero-padding used for convolution boundary handling
- **Time Complexity**: O(n×m) where n=height, m=width

## License

Coursework for image processing assignment.

---

**Author**: [@eisenheiim](https://github.com/eisenheiim)
