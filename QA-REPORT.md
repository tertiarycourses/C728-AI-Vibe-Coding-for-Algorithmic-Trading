# Independent C728 QA — 1 October 2026

Scope: C728 repository only. Read-only audit of current 75-slide PPT/PDF, 5-page LP DOCX/PDF, 22-page LG DOCX/PDF/Markdown, eight lab folders and build data. No deliverables edited.

## Initial findings — corrected and verified

1. **Medium — daily timing conflict.** `courseware/LP-C728-AI-Vibe-Coding-for-Algorithmic-Trading.pdf`, p4 Course Information and editable DOCX say 9:30–18:30, while the actual schedule tables begin 09:00 and end 18:00. Same incorrect timing appears on deck PDF slide 7. Sources: `build/build_lesson_plan.py` Daily Timing row; `build/build_slides.py` schedule slide.
2. **Medium — instructional duration conflict.** Deck PDF slide 7 title says “2 Days, 8 hours/day”, while the LP correctly reports 7.5 instructional hours/day, 15 instructional hours total. Eight hours is scheduled time excluding lunch and includes 30 minutes tea. Label scheduled versus instructional clearly.
3. **Medium — Lab 5 allocated duration mismatch.** `labs/lab-05-backtest/README.md:3` advertises 75 minutes, while `build/course_data.py` Day 2 and LP schedule allocate 10:00–10:45, 45 minutes. Adjust metadata or schedule consistently without changing validated 480/450-minute totals.

Latest readback verified deck slide 7 now says “2 Days, 15 instructional hours” and 09:00–18:00 with 30 minutes tea; LP p4 now uses matching timing and 7.5 instructional hours; Lab 5 README now states 45 minutes. No remaining medium/high defects.

## Final result — PASS

The low-severity LG doubled punctuation and Lab 5 templated description were corrected and verified in the latest LG Markdown/PDF and deck slide 52. Dependency versions are explicitly pinned. No unresolved audit findings remain.

## Passed checks

- Four topics map to Labs 1–2, 3–4, 5–6, 7–8 respectively; learning outcomes LO1–LO4 are consistently represented in slide recaps, LP and LG.
- Each day sums to 540 elapsed minutes = 60 lunch + 480 scheduled minutes; 480 includes 30 tea and yields 450 instructional minutes. Two days = 900 instructional minutes / 15 hours.
- All eight folders contain sample.py, prompt.md, readable one-page Prompt.pdf, detailed README and expected outputs. Each lab includes a Test it checkpoint and recovery route.
- Detailed commands and procedures appear in LG/README rather than the PPT. PPT has concept diagrams, worked fixtures, genuine generated indicator/backtest charts and compact lab outcome/checkpoint slides.
- All 75 rendered slides inspected through five contact sheets; detailed slide 7 and representative LP/LG pages inspected at larger size. No gross overflow, clipped headings, missing charts or overlapping objects detected.
- LP/LG covers, version record, populated TOC, headers, schedules and page numbers render. PPTX/DOCX ZIP integrity passes. All PDF extracted text blocks remain within page bounds.
- No assessment, SSG, WSQ, TRAQOM, funding or TGS programme wording found in public deliverable PDFs or prompt PDFs. No cross-course C-prefix identity found in checked public guides.

## Limits

This audit does not claim GitHub/Drive/storefront publication verification. Lab execution is assigned separately; this QA verifies instructions, checkpoints and package structure. The three timing findings were corrected by the parent agent and verified against latest rendered PDF/README readback.
