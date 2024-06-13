import unittest
from testmodels3.models import Product  # Adjust the import to your project's structure
from testmodels3 import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up a test database or any required initial state
        db.create_all()  # Ensure the database and tables are created
        self.product = Product(name="Test Product", description="This is a test product", price=9.99, stock=10)
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_delete_product(self):
        # Delete the product from the database
        product = Product.query.filter_by(name="Test Product").first()
        self.assertIsNotNone(product)

        db.session.delete(product)
        db.session.commit()

        # Verify the deletion
        deleted_product = Product.query.filter_by(name="Test Product").first()
        self.assertIsNone(deleted_product)

if __name__ == "__main__":
    unittest.main()
