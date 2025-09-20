# mini blog web application 
Develop a mini blog application using Flask to demonstrate CRUD operations and the interaction between Flask and HTML.:
Create a homepage (index.html) that displays a list of blog posts stored in a Python dictionary or list or csv or excel file.
Each blog post should have a title and a short description.
:
Create a form (add_post.html) to add a new blog post.
The form should include fields for:
Title
Description
Content (multi-line text input)
On submission, the form should send a POST request to the Flask backend, which adds the post to the data structure/csv file/excel file.:
Add a “Read More” button/link next to each blog post on the homepage.
Clicking the button should open a new page (view_post.html) that displays the complete content of the blog post.

Add an “Edit” button/link on the view_post.html page.
Clicking it should open a pre-filled form (edit_post.html) with the existing title, description, and content.
Update the data structure when the form is submitted.

Add a “Delete” button/link on the view_post.html page.
Clicking it should delete the blog post from the data structure and redirect back to the homepage.
Use Flask for backend logic.
Use HTML and Bootstrap for front-end design.
Handle all POST requests for creating, editing, and deleting posts.
Pass data between Flask and HTML pages using templates and context.
Add a timestamp to each post.
Implement basic validation (e.g., no empty fields).
Include a search bar on the homepage to filter posts by title.
Save blog posts in a CSV/Excel file for persistence.
