{
    "name": "Stock Move: Cancel & Reset to Draft Actions",
    "version": "16.0",
    "category": "Warehouse",
    "summery": "Add custom actions to cancel a stock move or reset it to draft directly from the stock move screen, improving control and error correction in inventory operations.",
    "description": """ This enhancement introduces two server-side actions on the stock.move model:
        Cancel Action
            Allows authorized users to cancel stock moves that are not yet completed.
            Automatically unreserves any reserved quantities before cancellation.
            Prevents cancellation of completed (done) moves to maintain inventory integrity.
        
        Reset to Draft Action
            Lets users revert a canceled stock move back to the draft state.
            Useful for correcting data entry mistakes or reprocessing previously canceled moves.
            Ensures the action is only available on canceled records.
            Both actions are integrated with the stock move interface via buttons, with visibility rules based on the current state of the move.
    """,

    "author": "Hi Spark Solutions",
    "company": "Hi Spark Solutions",
    "maintainer": "Hi Spark Solutions",
    "website": "https://www.hisparksolutions.com/",

    "depends": ["stock"],
    "demo": [],
    "data": [
        "views/stock_move_view.xml"
    ],
    "images": ["static/description/banner.gif"],
    "assets": {},
    "qweb": [],
    "live_test_url": "",

    "license": "OPL-1",
    "application": True,
    "auto_install": False,
    "installable": True,
    "price": "5",
    "currency": "USD",
}
