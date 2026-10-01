# C728 v1.0 publication verification

Verified on 1 October 2026. Course: **AI Vibe Coding for Algorithmic Trading**, non-WSQ C728. [Official registration page](https://www.tertiarycourses.com.sg/ai-vibe-coding-for-algorithmic-trading.html): 2 days / 15 instructional hours.

## Current deliverables

| Deliverable | Current package |
|---|---|
| Trainer/learner slides | 75-slide PPTX and matching PDF, v1.0 |
| Lesson Plan | 5-page PDF and editable DOCX |
| Learner Guide | 22-page PDF, editable DOCX and root Markdown mirror |
| Labs | Eight individual folders; each includes sample.py, prompt.md, Prompt.pdf and detailed README |

Detailed lab procedures are in the LG and lab READMEs. The PPT contains visual concepts, worked examples, actual generated charts and lab goals/checks. The supplied private C576 v10 reference was adapted to the four-topic C728 syllabus; the original reference remains unchanged and private.

## Quality and execution

- Independent rendered QA passed for all 75 slides and the LP/LG; timing and editorial defects were corrected and verified. See [QA report](QA-REPORT.md).
- All eight sample scripts executed successfully, including invalid-data, causal-signal, lag/cost, known-drawdown, chronological-selection and bot-control checks.
- Prohibited-content and credential scans passed; PPTX/DOCX XML was included in the credential scan.
- Python dependencies are pinned to the versions used for verification.
- The core lab pipeline uses synthetic observations. The optional authenticated Alpaca paper-account call was not executed with a real account; its endpoint and headers were checked against [official Get Account documentation](https://docs.alpaca.markets/us/reference/getaccount-1). No sample submits broker orders.

## Google Drive

[Verified C728 course folder](https://drive.google.com/drive/folders/1zRXCgZi8pBRThORwlvmiHiYbg_3FhhIX).

- All **52 current uploaded files** match local MD5 checksums: 6 main courseware files plus 46 lab-tree files.
- Four old deck IDs are preserved in archive folders; no old deck was deleted.
- The established [Activities folder](https://drive.google.com/drive/folders/1JA76jUDx5Niw6t5OfDS4E4hPsI6Lhfvf) carries the eight labs with its original name and ID; no duplicate folder was created.
- Existing notebook and two CSV datasets retain their original IDs. Trainer Resources and Brochure were outside the upload scope.
- Anonymous downloads of all six main files, all eight prompt PDFs, all eight sample scripts and the shared Python module match local checksums. The lab folder is anonymously browsable. Drive's standard Python-file download confirmation was followed during verification.

## Live storefront record

The C728 record on tertiarycourses.com.sg was read before and after the update. All **six links** were verified against the uploaded Drive IDs:

| Field | Verified target |
|---|---|
| Trainer Slides | [v1.0 PPTX](https://drive.google.com/file/d/19pXBejrkkZZRO3wdUbrz5gEYhUBnbAKI/view) |
| Learner Slides | [v1.0 PDF](https://drive.google.com/file/d/19lRr6rSWL0UmOwYGfrHqgrtOu9SM1115/view) |
| Lesson Plan | [Current LP PDF](https://drive.google.com/file/d/1gPjBsWFLg0ptAMa-QtQ3yh-94ZFbUhhi/view) |
| Learner Guide | [Current LG PDF](https://drive.google.com/file/d/1Dx2Ll56NOTTcQOCHIEHfyaB5CRoVSB12/view) |
| Lab URL | Established Activities folder |
| Courseware Link | Verified C728 course root |

The brochure link, product ID and course title were preserved. The protected before-state snapshot was removed only after successful live verification.

## GitHub

[Public repository](https://github.com/tertiarycourses/C728-AI-Vibe-Coding-for-Algorithmic-Trading), branch **main**. Initial courseware commit: **cc44a3f9b04d00eb5e7219d5098a8430b3632b92**. All 73 initial public file blobs were compared with local Git hashes, including all six editable/PDF courseware files and the complete labs tree. This publication report is added in a subsequent documentation commit.

README includes registration, course facts, purpose, outcomes, topics, each linked lab, all current courseware formats, usage and privacy boundaries, and provider attribution.

Verified About description: “Non-WSQ C728: AI Vibe Coding for Algorithmic Trading. Two days / 15 hours with Python research and paper-trading labs.” Homepage is the official registration URL above. Topics: `non-wsq`, `courseware`, `algorithmic-trading`, `python`, `ai-assisted-coding`. Discussions enabled; repository visibility public.

`reference/` is excluded from GitHub and Drive publication; no formal assessment package was created or published. Credentials, private environment files, dependencies and superseded archives are excluded from GitHub. No unresolved publication exception remains.
