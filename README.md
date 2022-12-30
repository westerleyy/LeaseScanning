# Lease Scan  
  
### Overview  
Details hidden in documents are hard to extract in a consistent and accurate manner. This task is easily automated in a machine-readable document. However, what happens if there are documents that are not machine-readable? If they are formatted consistently, and the details required are found in the same place, then a generalized data extraction model can be created to do this repetitive task. The problem arises when the documents are formatted similarly but not identically.  
  
In such a scenario, a position-based data extraction model falls terribly short. Other proxies will have to be relied upon to perform the data extraction. A text-based approach will have to be taken.  
  
### Text as Data  
Using computer vision, documents are scanned and converted to plain text. This renders documents quasi machine-readable. However, the data are unstructured. This does not mean that there is no structure in the data. Rather, the structure cannot be discerned easily by the machine. Instead, structure has to be afforded by the end user. Since the objective is to extract certain data points from the unstructured text, and there is some structure to the mass of text, Regular Expression can be used to extract the data.  
  
In a perfect world, this will suffice. Regular Expression will be able to determine the starting and ending characters with perfect accuracy. Yet, given the imperfect nature of data obtained through computer vision and the differences in formatting, Regular Expression and Computer Vision can only get us 70% of the way there. This leaves the end-user with a shorter amount of unstructured text to parse through. An improvement, but not the desired result.  
  
### BERT  
The text processing model, BERT, designed by Google AI can be used to close the outstanding last mile. How so? Using tiny-roberta, a model on Hugging Face, a chatbot with a Q&A function can be deployed fairly easily. Pass in a paragraph of text, and ask the bot a question. A question that is relevant to the text. In this case, the paragraph will be the text given to us by the previous step, Regular Expression. This is especially useful if the specific details required are the same for every single document. This implies that it can be scaled up pretty quickly. And this is what we have done here. 
