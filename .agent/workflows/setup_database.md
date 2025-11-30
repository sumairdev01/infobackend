---
description: How to set up a PostgreSQL database on Neon and connect it to Vercel
---

# Setting up a Database (Neon)

Since Vercel doesn't provide a database, we will use **Neon** (it's free and excellent for Postgres).

## Step 1: Create Database on Neon
1.  Go to [Neon.tech](https://neon.tech) and Sign Up.
2.  Click **"Create Project"**.
3.  Name it `portfolio-db` (or anything you like).
4.  Select the **Free Tier**.
5.  Click **Create Project**.
6.  **IMPORTANT:** Copy the **Connection String** (it looks like `postgres://user:password@...`). You will need this!

## Step 2: Deploy Backend to Vercel
1.  Go to [Vercel Dashboard](https://vercel.com/dashboard).
2.  **Add New...** -> **Project**.
3.  Import your `portfoliobackend` repository.
4.  **Environment Variables**:
    - Click on **Environment Variables** section (before clicking Deploy).
    - Add a new variable:
        - **Name**: `DATABASE_URL`
        - **Value**: (Paste the Connection String you copied from Neon)
        - **Name**: `SECRET_KEY`
        - **Value**: (Type a random string, e.g., `my-super-secret-key-123`)
        - **Name**: `DEBUG`
        - **Value**: `False`
5.  Click **Deploy**.

## Step 3: Run Migrations (Create Tables)
After deployment, your database is empty. You need to create the tables.
Since we can't easily run commands on Vercel, the easiest way is to connect from your local computer:

1.  In your local terminal (`f:\sumair-portfolio\backend`), create a `.env` file if you don't have one.
2.  Add `DATABASE_URL=your_neon_connection_string` to it.
3.  Run:
    ```bash
    python manage.py migrate
    ```
    (This will create the tables in your Neon database).

Now your backend is live with a working database!
