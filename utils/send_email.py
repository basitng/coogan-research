from email.message import EmailMessage
import ssl
import smtplib
import os


def send_email(csv_path, vtt_path, file_path, receiver_email):
    email_sender = "basitng2004@gmail.com"
    email_password = 'qgjeiajbneykzbgl'
    email_receiver = receiver_email
    subject = "Video Transcription"
    body = '''Congrats! your video has successfully been transcribed and correctly generated quality and corresponding image that suits the various sentences of the video. The CSV contains all the images and prompts.
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
