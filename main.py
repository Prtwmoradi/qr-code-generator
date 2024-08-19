import qrcode

# URL and header data
url = "https://resolver-dv1.gs1.org/gtin/888392335937?linktype=defaultLink"
headers = "Accept: application/linkset+json"

# Combine URL and headers into a single string for QR code
data_to_encode = f"{url}\n{headers}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_to_encode)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')
img.show()