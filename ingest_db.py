{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1R2CWSmPG_4-dZ9mTUAjRBnBH3k7TdnAk",
      "authorship_tag": "ABX9TyMP3TQXJ54ewO3c5DyMB/kq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/muqriher72/vendor_performance_analytics/blob/main/ingest_db_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "wRZNhU-e8gmD"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import os\n",
        "from sqlalchemy import create_engine\n",
        "import logging\n",
        "import time\n",
        "\n",
        "logging.basicConfig(\n",
        "    filename = \"logs/ingestion_db.log\"\n",
        "    level = logging.DEBUG,\n",
        "    format = \"%(asctime)s - %(levelname)s - %(message)s\",\n",
        "    filemode = \"a\"\n",
        ")\n",
        "\n",
        "engine = create_engine('sqlite:///inventory.db')\n",
        "\n",
        "'''This function will ingest the dataframe into database table'''\n",
        "def ingest_db(df, table_name, engine):\n",
        "    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)\n",
        "\n",
        "'''This function will load the CSVs as a dataframe and ingest into the database'''\n",
        "def load_raw_data():\n",
        "  start = time.time()\n",
        "  for file in os.listdir('data'):\n",
        "      if '.csv' in file:\n",
        "          df = pd.read_csv('data/'+file)\n",
        "          logging.info(f'Ingesting {file} in db')\n",
        "          ingest_db(df, file[:-4], engine)\n",
        "  end = time.time()\n",
        "  total_time = (end - start)/60\n",
        "  logging.info('----------------Ingestion Complete------------')\n",
        "  logging.info(f'Total Time Taken: {total_time} minutes')\n",
        "\n",
        "  if __name__ == '__main__':\n",
        "    load_raw_data()"
      ]
    }
  ]
}
