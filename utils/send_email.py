from email.message import EmailMessage
import ssl
import smtplib
import os


def send_email(csv_path, vtt_path, file_path, receiver_email):
    email_sender = "basitng2004@gmail.com"
    email_password = 'qgjeiajbneykzbgl'
    email_receiver = receiver_email
    subject = "Video Transcription"
    body = f'''Dear {receiver_email.split("@")[0]},

I hope this email finds you well. I am thrilled to inform you of the successful completion of your video transcription and image generation project. Our team has diligently worked on this task, and I'm delighted to report that we have achieved excellent results.

The video you provided has been accurately transcribed, capturing all the spoken content with precision. Our transcription process ensures a high level of accuracy, allowing you to easily reference and utilize the text-based representation of your video.

Additionally, we have successfully generated high-quality images that correspond to various sentences and prompts within the video. Each image has been carefully selected to suit the context and enhance the visual experience for your audience.

To facilitate your access to the generated images and associated prompts, we have conveniently compiled them into a comprehensive CSV file. This file contains all the necessary details, allowing you to efficiently organize and utilize the images in accordance with your specific requirements.

If you have any questions, require further assistance, or would like any additional information, please don't hesitate to reach out to our team. We are here to ensure your complete satisfaction and provide any necessary support.

Thank you for choosing our services for your video transcription and image generation needs. We greatly appreciate your trust in our capabilities, and we look forward to assisting you with any future projects.

Best regards,

Ajaga Abdulbasit
Coogan Research,
basitng2004@gmail.com.
    '''

    # create an EmailMessage object
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # attach the VTT file
    filename = os.path.basename(vtt_path)
    with open(vtt_path, 'rb') as f:
        file_data = f.read()
        em.add_attachment(file_data, maintype='text',
                          subtype='vtt', filename=filename)
    # attach the PDF file
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        file_data = f.read()
        em.add_attachment(file_data, maintype='text',
                          subtype='pdf', filename=filename)

    # attach the CSV file
    filename2 = os.path.basename(csv_path)
    with open(csv_path, 'rb') as f:
        file_data = f.read()
        em.add_attachment(file_data, maintype='text',
                          subtype='csv', filename=filename2)

    # create a secure SSL context and send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
