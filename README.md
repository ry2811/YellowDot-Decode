# Yellow Dots Decoder

A Python tool to detect and visualize yellow tracking dots (Machine Identification Code) embedded in printed documents by color laser printers and photocopiers.

## 🔍 What are Yellow Dots?

Many color laser printers and photocopiers secretly embed nearly invisible yellow dots on every printed page. These dots encode information such as:
- Printer serial number
- Date and time of printing
- Other identifying information

This tool helps detect and visualize these hidden tracking dots for security research and privacy awareness purposes.

## ✨ Features

- 🎨 HSV color space filtering to isolate yellow dots
- 🔬 High-contrast visualization of detected patterns
- 🖼️ Automatic image resizing for display
- 💻 Simple command-line interface

## 📋 Requirements

- Python 3.6+
- OpenCV (cv2)
- NumPy

## 🚀 Installation

 Clone this repository:
```bash
git clone https://github.com/ry2811/YellowDot-Decode.git
cd yellow-dots-decoder
```


## 💡 Usage

```bash
python yellow_dots_decode.py <image_path>
```

### Example:
```bash
python yellow_dots_decode.py scan.png
```

Or on Windows:
```bash
python yellow_dots_decode.py C:\Documents\scan.png
```

### Tips for best results:
- Use high-resolution scans (600 DPI or higher)
- Scan a blank area of printed paper for clearer dots
- Ensure good lighting and minimal noise in the scan

## 📸 How It Works

1. **Read Image**: Loads the scanned document
2. **Color Space Conversion**: Converts BGR to HSV for better color filtering
3. **Yellow Detection**: Uses HSV range `[20, 100, 100]` to `[40, 255, 255]` to isolate yellow
4. **Visualization**: Displays detected yellow regions in a mask
### "No dots detected"
- Ensure your scan is high resolution (≥600 DPI)
- The HSV range may need adjustment for different paper/printer types
- Try scanning a completely blank printed page

### "Image not found"
- Check the file path is correct
- Use forward slashes `/` or escaped backslashes `\\` in paths

## 📚 References

- [EFF: Tracking Dots](https://www.eff.org/pages/list-printers-which-do-or-do-not-display-tracking-dots)
- [Machine Identification Code](https://en.wikipedia.org/wiki/Machine_Identification_Code)

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---
