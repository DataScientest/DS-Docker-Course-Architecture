# Docker running project: starting point

🇫🇷 *Version française : branche [`fr`](https://github.com/DataScientest/DS-Docker-Course-Architecture/tree/fr).*

This repository is your starting point for the hands-on project of the Docker module. By the end of the module, it will run three containers connected by Docker Compose:

- **`db`**: a MariaDB database, which holds 1,000 customer transactions;
- **`train`**: a one-off job that trains a fraud detection model on these transactions;
- **`api`**: a FastAPI web API that gives access to the transactions and to the model's predictions.

All the code (Python, SQL) is provided: you only write the Docker part. Follow the course step by step: it tells you when and how to complete each file.

## Repository contents

```
DS-Docker-Course-Architecture/
├── step2-first-dockerfile/       the step 2 warm-up exercise (not part of the project)
│   ├── hello.py
│   ├── requirements.txt
│   └── Dockerfile                ✏️ fill-in-the-blanks template (step 2)
│
├── api/                          api service: the FastAPI application
│   ├── main.py                   the application (provided)
│   ├── requirements.txt          its dependencies (✏️ one line to add in step 8)
│   ├── Dockerfile                ✏️ to write (step 4)
│   └── .dockerignore             ✏️ to complete (step 4)
├── db/                           db service: the MariaDB database
│   ├── Dockerfile                ✏️ to write (step 5)
│   ├── init/
│   │   └── 01_transactions.sql   creates the table and loads the CSV into it (provided)
│   └── data/
│       └── transactions.csv      1,000 fictitious customer transactions (provided)
├── train/                        train service: model training
│   ├── train.py                  the training script (provided)
│   ├── requirements.txt          its dependencies (provided)
│   ├── Dockerfile                ✏️ to write (step 8)
│   └── .dockerignore             ✏️ to complete (step 8)
└── compose.yaml                  ✏️ to write (steps 6 and 8)
```

Each service has its own folder, named after it, which contains its Dockerfile. The `step2-first-dockerfile/` folder is not part of the project: it is the step 2 exercise.

## What you will complete

The files marked ✏️ only contain comments for now, which describe what they must contain.

| File | Step | What to do |
|---|---|---|
| `step2-first-dockerfile/Dockerfile` | 2 | Replace each `_____` with the right instruction |
| `api/Dockerfile` | 4 | Write, under each comment, the corresponding instruction |
| `api/.dockerignore` | 4 | List the files that must not be copied into the image |
| `db/Dockerfile` | 5 | Start from the official MariaDB image and add the scripts and data to it |
| `compose.yaml` | 6 | Describe the `db` and `api` services, their volume and their startup order |
| `train/Dockerfile`, `train/.dockerignore` | 8 | Write them, based on the specifications in the course |
| `compose.yaml`, `api/requirements.txt` | 8 | Add the `train` service and connect the model to the API |

You do not need to modify the other files.

## The provided programs

| Program | How to start it | Configuration (environment variables) |
|---|---|---|
| `api/main.py` | `uvicorn main:app --host 0.0.0.0 --port 8000` | `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `MODEL_PATH` |
| `train/train.py` | `python train.py` | The same `DB_*` variables, and `MODEL_PATH` |

Each variable is described at the top of each program. Once the API is running, its interactive documentation is available at `/docs`.

## Resources

- The [Docker cheat sheet](https://drive.google.com/file/d/1daIaVPO422omOqWVgqnzwZKexJH7Iz6U/view?usp=sharing): a PDF of six sheets with the commands, file templates and solutions to the most common errors.
- The official Docker documentation: https://docs.docker.com
- The solution is published in the [DS-Docker-Course-Solution](https://github.com/DataScientest/DS-Docker-Course-Solution) repository: it is the final project, as it should be at the end of step 8. Use it to compare with your work once a step is done, not to avoid searching.
