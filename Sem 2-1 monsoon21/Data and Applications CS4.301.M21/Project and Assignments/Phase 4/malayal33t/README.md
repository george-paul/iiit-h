# Data and Applications Project (Phase 4)
## Setup

In MySQL shell run `source '<path-to-project-folder>/malayal33t/UstadHotel.sql'`

Next run `python <path-to-project-folder>/malayal33t/CLI.py` to start the menu based program that manipulates the _Ustad Hotel_ database.

## Updates

* **When a customer arrives:** In the `Customer` table, the `Arrived` field of the corresponding tuple is changed to `True`.

* **When a reservation is postponed:** The `Start_End` and `Reservation` tables are updated to the new time.

* **When a dish gets delivered:** The `Status` field of the corresponding tuple in the `Dish` table is changed to `Delivered`.

## Queries (Retrievals)
* **View all reservations:** The `Reservation` table is accessed and all its tuples are shown (including completed and pending reservations).

* **View all menu items:** All items available to be ordered are shown.

* **Generate Total:** The total of the prices of the dishes ordered in an order.

* **All overdue dishes:** All dishes for which the ETA (listed in `Taken_ETA`) is *before* the current time are listed.

* **Total income** (over a day)**:** All orders made during the day are found, their prices are summed up and the total is printed.
