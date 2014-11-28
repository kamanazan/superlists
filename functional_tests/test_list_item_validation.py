from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    #@skip #did not work in python 2
    def test_cannot_add_empty_list_item(self):
        #raise SkipTest("NOT YET!!")
        # Edith goes to the home page adn accidentally tries to submit
        # an empty lists item. She hits Enter on empty input box

        # The home page refreshes, and there is an error message saying
        # that list item cannot be blank

        # She tries again with some text for the item, which now works

        # Preversely, she now decides to submit a second blank list item

        # She reveives a similar warning on the list page

        # And she can correct it by filling some text in the field
        self.fail('write me')

