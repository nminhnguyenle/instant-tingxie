# Instant Tingxie (听写)

Our submission for the Hack United v4 hackathon. 


## Inspiration

In our Chinese classes, we have weekly spelling tests (听写 tingxie) to test our knowledge and vocabulary on various words. We were inspired to create a more efficient and accurate way to practice for these tests, leading us to develop a website that enables students to easily prepare for these spelling tests.

## What it does

This website enables students to generate and grade practice papers by uploading an image of their word list. This method simplifies practice for students in our school, making it more accessible and efficient for students.

## How we built it

We used Flask and Python to build the backend for our website. The website design is made using a combination of custom CSS and the Bootstrap library. We used PaddleOCR to read the text from the input images, after trying and testing a variety of OCR solutions for accuracy when reading both Chinese and English characters. We were also considering using a multimodal AI such as Google Gemini to read the input, as during our testing we found that it also provided reasonable accuracy.

The PDF generation is a two-step process: first, we use python-docx to create and edit a new Microsoft Word file. In this file we add the headings, table, etc, after which we save it to a temporary directory and use command-line tools to convert this Word file into a PDF. Currently, we are using rocketpdf, however we were also considering pypandoc if we were to host our server on a supported Linux environment.

For the grading process, we were planning on using Google Gemini multimodal input to read the characters, and then compare the Gemini input to the original list, however, we were unfortunately unable to achieve this in time for submission.

## Challenges we ran into

During this hackathon, we faced challenges in accurately detecting and formatting text extracted from images. Integrating our front-end and back-end proved to be very challenging as well.

## Accomplishments that we're proud of

We are proud of our discipline in overcoming challenges within the allocated time. We are also proud of our AI text-detection integration, which required hours of fine-tuning through trial and error.

## What we learned

In this hackathon, we learned a lot about writing and text-detection including different OCR libraries, preprocessing techniques for images, and post-processing methods in order to improve text accuracy. We also learned how to approach and solve complex technical problems under pressure.

## What's next for Instant Tingxie

After this hackathon, we plan to further polish our text-detection system and add more features such as flashcards and compatibility with other apps such as quizlet and anki.
