Python 3.13.

Student Task: Build a Flexible API Using ViewSets and Dynamic Serializers
Create a model (e.g., Article with title, content, author, published).

Create a ModelSerializer with dynamic fields:

Allow the serializer to include only selected fields (e.g., via query params like ?fields=title,author).
Use a ViewSet to handle all CRUD operations for the Article model.

Use DefaultRouter or SimpleRouter to auto-generate the routes.

🔍 Example Output:
GET /articles/?fields=title,author → returns only title and author for each article.
GET /articles/1/ → returns full details of article with ID 1.
POST /articles/ → creates a new article.