# Advanced MLOps Exercise



## Part 7 — Main Branch Protection

Branch protection settings selected for `main`:

Restrict deletions
Only allow users with bypass permissions to delete matching refs.

Require a pull request before merging
Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.

Require status checks to pass
Choose which status checks must pass before the ref is updated. When enabled, commits must first be pushed to another ref where the checks pass.


Block force pushes
Prevent users with push access from force pushing to refs.

Required settings:

* Pull Request required before merging
* Successful status checks required
* Direct development on `main` prevented


## Part 8 — Merge Strategy

Merge strategy used:

Squash and merge

Justification:
Clean history and easy to review 

## Part 10 — Docker Image 1.0.0

Docker build:

```bash
docker build -t student-ml-api:1.0.0 .
```

Docker run:

```bash
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0
```

Health verification:

```bash
curl http://localhost:5000/health
```

Result:

{"application":"student-ml-api","status":"healthy","version":"1.0.0"}

## Part 11 — Docker Image Inspection

```

Required information:

| Item                          | Value       |
| ----------------------------- | ----------- |
| Container ID                  | `1193c543d178` |
| Image ID                      | `sha256:1193c543d1788b02a16bd25c4159434f47fa3cf05fcc3e8444e49f6a55208b44` |
| Exposed port                  | `5000` |
| Running command               | `python app.py` |
| Application working directory | `/app` |

---

## Part 12 — Container Registry

Registry used:

```text
GitHub Container Registry (GHCR)
```

Image:

```text
ghcr.io/HEREEEEEE/student-ml-api:1.0.0
```

---

## Part 13 — Git Tag and Release Version

Git tag:

```text
v1.0.0
```

Docker image:

```text
student-ml-api:1.0.0
```

Relationship:

```text
v1.0.0
  ↓
student-ml-api:1.0.0
```

---

## Part 14 — Automated Release Workflow

Release workflow trigger:

```yaml
on:
  push:
    tags:
      - "v*.*.*"
```

---

## Part 15 — Release Pipeline

Release workflow:

```text
Version Tag
↓
Checkout
↓
Run Tests
↓
Authenticate to Registry
↓
Build Docker Image
↓
Apply Version Tag
↓
Push Docker Image
```

The Docker image version is automatically derived from the Git tag.



## Part 16 — Registry Verification

Registry contents after `v1.0.0`:

```text
student-ml-api
├── 1.0.0
└── latest
```

Image digest:



## Part 17 — Artifact Reproducibility

Local image deleted:

```bash
docker rmi student-ml-api:1.0.0
```

Image retrieved from registry:

```bash
docker pull ghcr.io/HEREEEEEE/student-ml-api:1.0.0
```

Health endpoint verification:

```bash
curl http://localhost:5000/health
```



## Part 18 — Version 1.1.0

Feature branch:

```text
feature/model-metadata
```

Updated `/health` response:

```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

Pull Request:



## Part 19 — Release Version 1.1.0

Git tag:

```text
v1.1.0
```

Registry contents:

```text
student-ml-api
├── 1.0.0
├── 1.1.0
└── latest
```

Verification that:

```text
latest → 1.1.0
```

and `1.0.0` remains available:



## Part 20 — Rollback

Problematic version:

```text
1.1.0
```

Known-good version:

```text
1.0.0
```

Image retrieved from registry:

```bash
docker pull ghcr.io/HEREEEEEE/student-ml-api:1.0.0
```

Container run:

```bash
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/HEREEEEEE/student-ml-api:1.0.0
```

Health verification:

```bash
curl http://localhost:5000/health
```


```

---

## Part 21 — Traceability Challenge

### Version 1.1.0

Pull Request:


Merge Commit SHA:


Git Tag:

```text
v1.1.0
```

Docker Image:

```text
ghcr.io/HEREEEEEE/student-ml-api:1.1.0
```

Docker Image Digest:



Complete chain:

```text
PR: 
↓
Merge Commit: 
↓
Git Tag: v1.1.0
↓
Docker Image: ghcr.io/HEREEEEEE/student-ml-api:1.1.0
↓
Image Digest: sha256:
```

---

## Part 22 — CI and Release Separation

### CI Workflow

Runs on:

```text
Pull Request
```

Responsibilities:

```text
Test
Validate
Build-check
```

The CI workflow does **not** publish a release artifact.

### Release Workflow

Runs on:

```text
Version Tag
```

Responsibilities:

```text
Test
Build
Version
Publish
```

Publishing is separated from CI because Pull Requests must first pass validation and code review before a release artifact is published.
