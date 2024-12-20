"""Main Streamlit application"""

import os
import streamlit as st
from model_handler import ModelHandler
from notification_service import NotificationService
from config import PRODUCT_LINKS

def main():
    st.title('Welcome to Apna Electrician')
    st.subheader('Upload or capture an image of a product, and get recommendations!')

    # Initialize services
    try:
        model_handler = ModelHandler()
        notification_service = NotificationService()
    except Exception as e:
        st.error(f"Service initialization failed: {e}")
        return

    # User input
    user_message = st.text_area("Enter a message for the electrician:")
    
    # Image input options
    captured_image = st.camera_input("Capture an image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if st.button("Upload and Send"):
        if (uploaded_file or captured_image) and user_message:
            try:
                # Save image
                os.makedirs('upload', exist_ok=True)
                save_path = os.path.join('upload', 
                    uploaded_file.name if uploaded_file else 'captured_image.jpg')
                
                image_data = uploaded_file if uploaded_file else captured_image
                with open(save_path, 'wb') as f:
                    f.write(image_data.getbuffer())

                # Display image
                st.image(save_path, caption="Selected Image", use_container_width=True)

                # Process image
                predicted_class, confidence = model_handler.predict(save_path)
                
                if predicted_class is None:
                    st.warning("Could not identify the product in the image. Please try again with a clearer image.")
                    return

                buy_link = PRODUCT_LINKS.get(predicted_class, 'https://www.apnaelectrician.com/')
                
                # Send notifications
                email_sent = notification_service.send_email(
                    save_path, predicted_class, buy_link, user_message)
                whatsapp_sent = notification_service.send_whatsapp(
                    predicted_class, buy_link)

                # Show results
                st.success(f"Product detected: {predicted_class} (Confidence: {confidence:.2%})")
                st.markdown(f"[Buy here]({buy_link})")
                
                if email_sent:
                    st.info("Email notification sent successfully!")
                if whatsapp_sent:
                    st.info("WhatsApp notification sent successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload or capture an image and enter a message before proceeding.")

    if st.button("Clear"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()