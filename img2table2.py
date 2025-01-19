from paddleocr import PPStructure, draw_structure_result, save_structure_res
import pandas as pd
from PIL import Image
import os
import cv2

# Initialize PP-Structure for table extraction
ppstructure = PPStructure(recovery=True, lang='ch')  # Use 'ch' for Chinese + English support

# Path to your image
image_path = 'example_additional.jpg'

# Perform table extraction
image = cv2.imread(image_path)
result = ppstructure(image)

# Extract table data from the result
for element in result:
    if element['type'] == 'table':  # Filter only table data
        table_data = element['res']  # Table content

        # Convert table data to a DataFrame
        df = pd.DataFrame(table_data)

        # Save to a CSV file
        csv_file_path = 'output.csv'
        df.to_csv(csv_file_path, index=False, header=False)

        print(f"Table data saved to {csv_file_path}")
