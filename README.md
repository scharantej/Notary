## Problem Summary
The task is to design a Flask application that allows users to take notes and organize them into folders. The application should include:
- A page for taking notes.
- A page for viewing notes.
- A page for managing folders.

## Solution Design
### HTML Files
- **notes_form.html**: This HTML file will contain the form for taking notes. It will have a text area for the note content, a select box for selecting the folder, and a submit button.
- **notes_list.html**: This HTML file will display the list of notes. It will have a table with columns for the note title, content, and folder.
- **folders_list.html**: This HTML file will display the list of folders. It will have a table with columns for the folder name and a link to view the notes in that folder.

### Routes
- **@app.route('/notes/new', methods=['GET', 'POST'])**: This route will handle the creation of new notes. When a GET request is made to this route, it will render the **notes_form.html** file. When a POST request is made, it will create a new note and redirect to the **notes_list.html** file.
- **@app.route('/notes/', methods=['GET'])**: This route will handle the display of the list of notes. It will render the **notes_list.html** file.
- **@app.route('/notes/<int:note_id>', methods=['GET'])**: This route will handle the display of an individual note. It will render the **notes_form.html** file with the pre-populated note content.
- **@app.route('/folders/', methods=['GET'])**: This route will handle the display of the list of folders. It will render the **folders_list.html** file.
- **@app.route('/folders/<int:folder_id>', methods=['GET'])**: This route will handle the display of the notes in a specific folder. It will render the **notes_list.html** file with only the notes that belong to the specified folder.