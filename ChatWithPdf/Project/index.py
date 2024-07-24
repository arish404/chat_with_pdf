from parsing import main
import google.generativeai as genai
from streamlit import write


def to_markdown(text):
  text = text.replace('•', ' ')
  return text

document_text=user_prompt=" "
result = main()
if result:
  genai.configure(api_key="YOUR_API_KEY")
  model = genai.GenerativeModel('gemini-pro')
  if result is not None:
    document_text,user_prompt = result
  if user_prompt=="":
    response = model.generate_content(document_text+"consider the text is from any files"+"generate any questions about the content")
  else:
    response = model.generate_content(document_text+"consider the text is from any files"+user_prompt)
  write(to_markdown(response.text))