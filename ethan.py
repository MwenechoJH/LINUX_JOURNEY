import cv2
import numpy as np

# HSV color ranges for brown, green, and red detection
COLOR_RANGES = {
    'Green': {
        'range': [(40, 40, 40), (80, 255, 255)],
        'display_color': (0, 255, 0)  # Green in BGR
    },
    'Red': {
        'ranges': [
            [(0, 100, 100), (10, 255, 255)],  # Lower red range
            [(160, 100, 100), (180, 255, 255)]  # Upper red range
        ],
        'display_color': (0, 0, 255)  # Red in BGR
    },
    'Brown': {
        'range': [(10, 100, 20), (20, 255, 200)],
        'display_color': (42, 42, 165)  # Brown in BGR
    }
}

# Detection parameters
MIN_BLOCK_AREA = 500       # Minimum pixel area to consider as a block
MIN_ASPECT_RATIO = 0.7     # Minimum width/height ratio for blocks
MAX_ASPECT_RATIO = 1.3     # Maximum width/height ratio for blocks

def create_color_mask(hsv_img, color_info):
    """Creates a mask for the specified color range"""
    if 'ranges' in color_info:  # Special handling for red
        lower1, upper1 = np.array(color_info['ranges'][0]), np.array(color_info['ranges'][0][1])
        lower2, upper2 = np.array(color_info['ranges'][1]), np.array(color_info['ranges'][1][1])
        mask1 = cv2.inRange(hsv_img, lower1, upper1)
        mask2 = cv2.inRange(hsv_img, lower2, upper2)
        return cv2.bitwise_or(mask1, mask2)
    else:
        lower, upper = np.array(color_info['range'][0]), np.array(color_info['range'][1])
        return cv2.inRange(hsv_img, lower, upper)

def detect_blocks(frame, mask, color_name, display_color):
    """Identifies rectangular blocks in the mask and annotates them"""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_BLOCK_AREA:
            continue
            
        # Get rotated bounding box
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        
        # Check aspect ratio
        width, height = rect[1]
        aspect_ratio = min(width, height) / max(width, height)
        if MIN_ASPECT_RATIO < aspect_ratio < MAX_ASPECT_RATIO:
            # Draw bounding box
            cv2.drawContours(frame, [box], 0, display_color, 2)
            
            # Add label at center
            M = cv2.moments(cnt)
            if M["m00"] > 0:
                cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
                cv2.putText(frame, f"{color_name} Block", (cx-50, cy), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, display_color, 2)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Detecting brown, green, and red blocks...")
    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Process each color
        for color_name, color_info in COLOR_RANGES.items():
            # Create color mask
            mask = create_color_mask(hsv, color_info)
            
            # Reduce noise
            kernel = np.ones((5,5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
            # Detect and draw blocks
            detect_blocks(frame, mask, color_name, color_info['display_color'])

        # Display result
        cv2.imshow("Block Detector", frame)
        
        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()