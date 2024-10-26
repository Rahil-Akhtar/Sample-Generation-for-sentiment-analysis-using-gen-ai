# import pandas as pd
# from openpyxl import Workbook
# from langchain_ollama import OllamaLLM

# # Initialize the Ollama model
# model = OllamaLLM(model="llama3")


# # Initialize a DataFrame to hold the results
# results = {'emotion': [], 'content': []}

# # Dictionary mapping emotions to their starting indices
# #emotion_indices = {
#     #'empty': 827,
#     #'enthusiasm': 759,
#    # 'hate': 1323,
#   #  'boredom': 179,
#  #   'anger': 110
# #}
# emotion_indices={
#      'empty': 827,
#     'enthusiasm': 759,
#     'hate': 1323,
#     'boredom': 179,
#     'anger': 110
# }
# # Define your sentiment_list
# sentiment_list = list(emotion_indices.keys())

# # Loop through the emotions and generate content
# for emotion in sentiment_list:
#     #start_index = emotion_indices.get(emotion, 0)  # Default to 0 if emotion not found
#     for i in range(1000):  # Adjust range as needed
#         prompt=f"Write a tweet with the {emotion} emotional tone, your response should only have the tweet noting else, donot leave the tweet empty, "

#         # Generate text using the model
#         response = model.invoke(prompt)

#         # Store the emotion and the generated response
#         results['emotion'].append(emotion)
#         results['content'].append(response)
#         print(f'DONE: {emotion}, ROW: {i}')
# print("FINISH")
# # Create a DataFrame from the results
# df = pd.DataFrame(results)

# # Save to an Excel file using openpyxl
# excel_file_path = 'output_data/balanced_classes1000.xlsx'  # Change the file name as needed
# with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
#     df.to_excel(writer, index=False, sheet_name='Emotions')

import pandas as pd
from openpyxl import Workbook
from langchain_ollama import OllamaLLM

# Initialize the Ollama model
model = OllamaLLM(model="llama3")

# Initialize the workbook and worksheet
workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'Balancing Emotional Classess'
worksheet.append(['Emotion', 'Content'])  # Add headers
excel_file_path = 'output_data/balanced_classes-thousand.xlsx'  # Change the file name as needed

# Dictionary mapping emotions to their starting indices
emotion_indices = {
    'empty': 827,
    'enthusiasm': 759,
    'boredom': 179,
    'anger': 110
}
# Define your sentiment_list
sentiment_list = list(emotion_indices.keys())

# Loop through the emotions and generate content
for emotion in sentiment_list:
    for i in range(1000):  # Adjust range as needed
        prompt = f"Write a tweet with the {emotion} emotional tone, your response should only have the tweet noting else, donot leave the tweet empty."

        # Generate text using the model
        response = model.invoke(prompt)

        # Store the emotion and the generated response in the worksheet
        worksheet.append([emotion, response])
        print(f'DONE: {emotion}, ROW: {i + 1}')  # Adjust row count for clarity
        if (i + 1) % 100 == 0:
           workbook.save(excel_file_path)
           print(f'Saved progress after {i + 1} rows.')

# Save the workbook to an Excel file
workbook.save(excel_file_path)
print("FINISH")