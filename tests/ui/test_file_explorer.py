default_page_size = 25

# Dialogs show for various actions (upload, delete, move, copy, etc.)
# Popups appear for table filtering
# Context menus appear for right-click actions on files/folders

def test_FE_can_view_all_files():
    # open browser
    # navigate to file explorer (can be direct URL or via Home Page UI -> Menu -> File Explorer)
    # Verify page is loaded (check for specific element such as title)
    # Verify table has at least 1 row (indicating files are present and table is loaded)
    # Retrieve from API or database all rows expected to be represented in table (table is paginated)
    # Build an expected UI representation of all rows
    # Extract from the UI the representation of all rows present on the page
    # Extract from UI the current pagination state (page number, page size)
    # Assert that the expected representation matches the UI representation

def test_FE_pagination():
    # Similar to above test, but focus on verifying pagination controls work correctly
    # There should be a verification that the database contains suficient rows to require pagination
    # The test should verify contents of first page
    # Then navigate to next page and verify contents again
    # Finally, navigate back to first page and verify contents again

def test_FE_pagination_with_sorting():
    # Similar to pagination test, but add sorting into the mix
    # Verify that sorting by first column works correctly for first page
    # Navigate to next page and verify sorting is still correct
    # Navigate back to first page and verify sorting is still correct

def test_FE_file_upload():
    # Test file upload functionality:
    # Retrieve current number of files in DB
    # Sort table by most recently added file
    # Assert table total rows matches DB count
    # Upload a file via the UI
    # Wait for upload to complete
    # Refresh the table
    # Assert table total rows is DB count + 1
    # Assert the newly uploaded file appears at the top of the table

# Other tests are to be added which will involve UI components such as dialogs, popups, and context menus and so on
# Also the tests may need to make use of helper functions such as:
# - determine the number of rows on a given page given parameters (page number, page size, total rows)
# - build expected UI representation of rows given a set of data and pagination/sorting/filtering/column ordering and visibility parameters
# - extract current pagination/sorting/filtering/column ordering and visibility state from the UI

# Also tests may need complex assertion functions, for example to:
# - assert that two representations of table rows match, taking into account pagination/sorting/filtering/column ordering and visibility settings
# - assert that dialogs/popups/context menus appear as expected and contain the correct options and information

# Page objects will be used to interact with the File Explorer UI components, encapsulating the logic for interacting the UI
# Locators will be hidden within the page objects to keep the tests clean and focused on behavior rather than implementation details
# waiting methods will be contained in the page objects to handle dynamic loading of UI elements, such as:
# - waiting for the table to load
# - waiting for dialogs/popups/context menus to appear and disappear
# - waiting for pagination/sorting/filtering actions to complete

