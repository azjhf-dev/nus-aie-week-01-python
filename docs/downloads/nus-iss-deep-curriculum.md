# Seven weeks of AI engineering, reconstructed from public evidence

Checked 19 November 2026. Independent self-study material, not an official NUS curriculum or credential.

## Answer

The public record is enough to build a useful learning programme, but not to recover private NUS teaching materials. The seven module names and published objectives come from NUS School of Computing. NUS-ISS repositories supply related implementation patterns, project artifacts and failure cases. They belong to different courses and cohorts, often at a different depth. The result is a 106-hour, seven-week self-study path, seven separate repositories, fourteen Marimo notebooks, original assessments and a source audit. One repository is a genuine MIT-licensed JobAId fork. The six others are original companion repositories.

## Start with these sources

1. **JobAId** for a modern, licensed implementation to inspect and fork. Its FSM transitions, review stages and retrieval paths are visible in actual code. It is not independently security-certified.
2. **WhatsEat backend plus project hub** for a concrete multi-agent/RAG system and report structure. It has several external-service requirements.
3. **bleongcw/generativeai_course** for the strongest modern teaching sequence found: prompts, tools, agents, embeddings, attention, RAG and evaluation. It is instructor material, not a student submission. No repository-wide license was detected, so link rather than copy.
4. **PRS healthcare project** for classical ML, forecasting, bill estimation, pipeline and serving examples. Use only the public code as a reference. Real healthcare data is neither needed nor re-published.
5. **Dog Breed Detective** for transfer learning and an instructive code-quality issue, not as unquestioned production-ready code.

## Scope and evidence labels

- **Official:** published NUS SoC SCTP programme/module objectives and classroom-day counts.
- **Related evidence:** student or teaching repositories from NUS-ISS or a different affiliated training programme.
- **Original design:** the seven-week pace, estimated hours, exercises, synthetic data, visuals, assessments and rubric.
- **Not recovered:** official slide decks, exact labs, marking weights, exam questions, hidden datasets or LMS materials.
- **Inspection:** all 24 curated entries had their complete available file trees checked and relevant README excerpts reviewed, except the speech collection with no readable README. Selected actual code/notebook cells were inspected for the stronger claims. This is not a line-by-line audit of all 24 codebases. No full upstream application or student benchmark was reproduced.

### Corrections to overconfident interpretations

The earlier search result should be read as **no exact-programme student submission found in that search**, not proof that no public repositories exist. Repository counts change and forks/templates can inflate them. The first-intake timeline and predicted capstone date are not needed to establish this learning path and are not used as evidence here. NTU entrance tests say nothing about the NUS programme entrance-test difficulty. NUS-ISS IRS/PRS and NUS SoC SCTP are not interchangeable.

## What the new repositories contain

Every week has `course.py` (interactive browser-capable mechanism notebook), `build_lab.py` (deeper local project notebook with an executed mobile-readable snapshot), `CURRICULUM.md`, `ASSESSMENT.md`, `LAB_LOG.md`, `SOURCES.md`, deterministic tests and installation instructions. The browser core has controllable SVG motion graphics, responsive charts, tables, sliders and explicit boundaries between real training and mechanism illustrations. Hosted browser interactivity downloads a Python runtime/packages and needs internet. Deeper PyTorch/LangGraph notebooks run locally; their hosted snapshots are read-only.

## The seven-week path

### Week 1: Python Programming for AI Engineering

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-python-programming-for-ai-engineering/

Official classroom days: 2. Original self-study estimate: 12 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-01-python

**Published scope, paraphrased:** Python data structures and constructs, files, simple applications, NumPy and pandas.

**Five-day build plan:**

- Day 1: expressions, types, collections and functions (2h)
- Day 2: file I/O, CSV and validation (2h)
- Day 3: NumPy arrays and vector operations (2h)
- Day 4: pandas cleaning and group summaries (2h)
- Day 5: build, test and explain the audit (4h)

**Core notebook experiments:**

- Inject controlled missingness into a synthetic table.
- Compare deletion, median and zero imputation.
- Inspect actual NumPy standardisation.
- Create and validate a CSV artifact.

**Deeper build notebook:** A real CSV parser checks raw duplicate headers before pandas can rename them, validates ranges and handles all-missing columns explicitly. Edit the input and observe rejected cases.

**Submit:** A reproducible synthetic learning-activity data audit. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/bhuiyanmobasshir94/NUS-Artificial-Intelligence-Training
- https://github.com/danieltanhx/IRS-PM-2020-01-18-IS02PT-GRP7-Smart-Job-Recommender-System

**Remaining boundary:** No exact SCTP Python assignments are public in the inspected evidence. The synthetic dataset and all lessons are original.

### Week 2: Applied Machine Learning

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-applied-machine-learning/

Official classroom days: 2. Original self-study estimate: 14 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-02-machine-learning

**Published scope, paraphrased:** End-to-end ML workflow, data preparation, classification/regression/prediction, validation and performance assessment.

**Five-day build plan:**

- Day 1: problem framing and split strategy (2h)
- Day 2: regression and gradient descent (3h)
- Day 3: logistic classification and thresholds (3h)
- Day 4: complexity, validation and leakage (2h)
- Day 5: error analysis and model card (4h)

**Core notebook experiments:**

- Train polynomial regression with gradient descent.
- Explore classifier thresholds and confusion matrices.
- Compute explicit false-positive/negative costs.
- Stress a model with corrupted inference features.

**Deeper build notebook:** A sklearn Pipeline compares majority, logistic and random-forest baselines using development cross-validation. Imputation/scaling fit inside each fold. A final held-out test is consulted after selection.

**Submit:** A held-out synthetic intervention classifier with a model card. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/ISS-IS02PT/PRS-PM-ISY5002-GROUP5
- https://github.com/bhuiyanmobasshir94/NUS-Artificial-Intelligence-Training
- https://github.com/IRS-PM/IRS-PM-2021-01-16-IS03PT-GRP-HDB-Resale-Price-Recommender

**Remaining boundary:** Student metrics are not treated as independently reproduced. The core uses transparent NumPy implementations; scikit-learn comparison is an extension.

### Week 3: Deep Learning and Neural Networks

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-deep-learning-and-neural-networks/

Official classroom days: 1. Original self-study estimate: 16 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-03-deep-learning

**Published scope, paraphrased:** Deep learning principles, CNNs for images, RNNs/Transformers for language, implementation and training using frameworks.

**Five-day build plan:**

- Day 1: tensors, activations and gradients (3h)
- Day 2: MLP training and failure modes (3h)
- Day 3: convolution and transfer learning (3h)
- Day 4: RNN state and attention (3h)
- Day 5: model comparison and report (4h)

**Core notebook experiments:**

- Train a two-layer XOR network with backpropagation.
- Inspect fixed convolution filters.
- Follow recurrent state.
- Compare causal and non-causal dot-product attention.

**Deeper build notebook:** Small PyTorch CNN, RNN and Transformer models actually train on seeded synthetic tasks with held-out rows. Their tasks differ, so their displayed accuracies must not be used to rank architectures.

**Submit:** A trained XOR network plus a documented sequence/vision experiment. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/IRS-PM/2023-05-25-Dog-Breed-Detective
- https://github.com/NUS-AIS-Practice-Modules/PRS-PM-2025-10-15-18FT-GRP-NeverStopCoding-M3
- https://github.com/aaxwaz/NUS_ISS_DeepLearningWorkshop

**Remaining boundary:** The browser core teaches mechanisms; build_lab.py actually trains small CNN, RNN and Transformer models on synthetic tasks. Pretrained models, natural-language/image benchmarks and full-scale training are not bundled.

### Week 4: Generative AI and its Applications

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-generative-ai-and-its-applications/

Official classroom days: 2. Original self-study estimate: 16 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-04-generative-ai

**Published scope, paraphrased:** Autoencoders and generative models, image generation, BERT/GPT, multimodal applications and hands-on projects.

**Five-day build plan:**

- Day 1: reconstruction and autoencoding (3h)
- Day 2: latent controls and denoising (3h)
- Day 3: token probabilities and text objectives (3h)
- Day 4: multimodal alignment and responsible use (3h)
- Day 5: gallery, evaluation and limitations (4h)

**Core notebook experiments:**

- Train a nonlinear autoencoder.
- Separate forward corruption from simplistic smoothing.
- Explore entropy and temperature.
- Inspect synthetic cross-modal embedding alignment.

**Deeper build notebook:** Actual CPU training of a VAE and a 2D DDPM, plus tiny masked/causal Transformer objectives. These are not pretrained BERT, GPT or Stable Diffusion. Sampling from two-dimensional distributions does not establish image-generation ability.

**Submit:** A transparent generative-model gallery with failure notes. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/IRS-PM/IRS-PM-2023-08-21-GRP19-Rebalancing-Data-Research
- https://github.com/bleongcw/generativeai_course
- https://github.com/NUS-AIS-Practice-Modules/PRS-PM-2025-10-15-18FT-GRP-NeverStopCoding-M3

**Remaining boundary:** Toy denoising is not Stable Diffusion. Sampling from a small fixed vocabulary is not GPT; no pretrained BERT/GPT or multimodal model inference is bundled. The official named model families need the documented optional extensions.

### Week 5: Large Language Models and Agentic AI

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-large-language-models-and-agentic-ai/

Official classroom days: 2. Original self-study estimate: 16 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-05-llm-agents

**Published scope, paraphrased:** LLM overview, prompt engineering, chatbots, RAG and agentic workflows.

**Five-day build plan:**

- Day 1: tokens, prompts and context budgets (3h)
- Day 2: TF-IDF retrieval, chunking and evaluation (3h)
- Day 3: grounded extractive answers and abstention (3h)
- Day 4: state machines, tool budgets and human review (3h)
- Day 5: inspect the real JobAId fork and write a test report (4h)

**Core notebook experiments:**

- Retrieve authored evidence using TF-IDF cosine similarity.
- Build extractive answers with source IDs and abstention.
- Inspect a bounded FSM with human review.
- Score retrieval independently from answer style.

**Deeper build notebook:** An actual LangGraph StateGraph pauses at an interrupt and resumes through a checkpointer after a demo review decision. Nodes are deterministic and make no LLM calls. The inherited JobAId app remains available for separate study.

**Submit:** A synthetic study-resource assistant with retrieval evaluation. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/anastasiapatricks/JobAId
- https://github.com/NUS-AIS-Practice-Modules/WhatsEat-backend-LangGraph-supervisor-py
- https://github.com/NUS-AIS-Practice-Modules/CryptoPulse
- https://github.com/bleongcw/generativeai_course

**Remaining boundary:** The no-key core uses extractive answers and a deterministic FSM, not an LLM. The inherited JobAId application is real LangGraph/FastAPI code but its external-service integration has not been executed or security-certified here.

### Week 6: Model Deployment and MLOps Essentials

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-model-deployment-and-mlops-essentials/

Official classroom days: 1. Original self-study estimate: 12 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-06-mlops

**Published scope, paraphrased:** Production deployment, MLOps process, monitoring, maintenance and efficient operations.

**Five-day build plan:**

- Day 1: inference schema and reproducible artifacts (2h)
- Day 2: serve and validate locally (2h)
- Day 3: latency and monitoring (2h)
- Day 4: drift and rollout simulation (2h)
- Day 5: incident drill and runbook (4h)

**Core notebook experiments:**

- Validate an inference JSON contract.
- Reject bad values and unknown fields.
- Compare common-bin distributions with PSI.
- Gate a rollout against declared error and latency assumptions.

**Deeper build notebook:** A real loopback HTTP service is started on an ephemeral port, measured and stopped. Tests exercise health, valid prediction and invalid JSON. A runbook covers a local version/rollback drill, not a production deployment.

**Submit:** A local standard-library prediction API and monitoring card. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/anastasiapatricks/JobAId
- https://github.com/NUS-AIS-Practice-Modules/WhatsEat-backend-LangGraph-supervisor-py
- https://github.com/ISS-IS02PT/PRS-PM-ISY5002-GROUP5

**Remaining boundary:** No strong exact-course production MLOps submission was found. Hosted pages run notebooks in the browser; they are not model-serving production deployments. No cloud resources are purchased.

### Week 7: Capstone Project for AI Engineering

Official anchor: https://www.comp.nus.edu.sg/executive-education/course/sctp-capstone-project-for-ai-engineering/

Official classroom days: 3. Original self-study estimate: 20 active hours. Learning repository: https://github.com/azjhf-dev/nus-aie-week-07-capstone

**Published scope, paraphrased:** Group problem definition, tailored implementation, data acquisition/preparation, validation, documentation and stakeholder presentation.

**Five-day build plan:**

- Day 1: scope, dataset card and evaluation plan (3h)
- Day 2: baseline pipeline and user interface (4h)
- Day 3: predictor plus retrieval integration (4h)
- Day 4: evaluation, incident drill and fairness caveats (4h)
- Day 5: clean rerun, report and five-minute demo (5h)

**Core notebook experiments:**

- Declare a recall gate before inspecting outcomes.
- Inspect errors by synthetic groups without claiming fairness certification.
- Add a source-traced study-resource helper.
- Track release evidence and unresolved risks.

**Deeper build notebook:** A fixed 240/80/80 split fits logistic weights, selects a threshold on validation cost, then reports a locked final test and an artifact fingerprint. Retrieval evaluation is separate. Repeated tuning invalidates final-test status.

**Submit:** Study-support demonstrator, using only synthetic records and a tiny authored corpus. Include changed-control observations, tests, a failure analysis and a short explanation.

**Related evidence:**

- https://github.com/anastasiapatricks/JobAId
- https://github.com/NUS-AIS-Practice-Modules/IRS-PM-2025-08-30-AIS11FT-GRP-NeverStopCoding-WhatsEat
- https://github.com/atsui888/MTech-AI-Capstone-Project
- https://github.com/IRS-PM/Workshop-Project-Submission-Template

**Remaining boundary:** Assessment weights, expected capstone size, official datasets and marking rubrics are unpublished in the evidence inspected. The rubric supplied here is an original self-study rubric, not NUS's.

## Source audit: useful artifacts and traps

### NUS-AIS-Practice-Modules/IRS-PM-2025-08-30-AIS11FT-GRP-NeverStopCoding-WhatsEat

https://github.com/NUS-AIS-Practice-Modules/IRS-PM-2025-08-30-AIS11FT-GRP-NeverStopCoding-WhatsEat

Type: student project/report. Maps to weeks 5;7. License metadata: NONE-DETECTED.

Entry point: `projectReport/IRS-PM-2025-08-30-AIS11FT-GRP-NeverStopCoding-WhatsEat-Group-Report.pdf`.

Practice-module heading explicitly names IRS; README and report tree describe a multi-agent restaurant assistant.

**Caution:** Project-report hub; implementation is split into separate repositories. Report PDF not independently audited end to end.

### NUS-AIS-Practice-Modules/WhatsEat-frontend-agent-chat-ui

https://github.com/NUS-AIS-Practice-Modules/WhatsEat-frontend-agent-chat-ui

Type: student implementation, upstream fork. Maps to weeks 5;6;7. License metadata: MIT.

Entry point: `src/hooks/use_langgraph_chat.ts`.

README explains a React chat UI connected to the LangGraph backend.

**Caution:** Frontend alone does not establish agent or RAG correctness; forked UI scaffolding is not all original student work.

### NUS-AIS-Practice-Modules/WhatsEat-backend-LangGraph-supervisor-py

https://github.com/NUS-AIS-Practice-Modules/WhatsEat-backend-LangGraph-supervisor-py

Type: student implementation, upstream fork. Maps to weeks 5;6;7. License metadata: MIT.

Entry point: `whats_eat/app/supervisor_app.py`.

Inspected actual supervisor and RAG-agent code: coordinated agents, tool lists and a retrieval/ranking path.

**Caution:** MIT notice is inherited from LangChain. Multiple external services and credentials are needed for the full app; not run here.

### NUS-AIS-Practice-Modules/PRS-PM-2025-10-15-18FT-GRP-NeverStopCoding-M3

https://github.com/NUS-AIS-Practice-Modules/PRS-PM-2025-10-15-18FT-GRP-NeverStopCoding-M3

Type: student notebook collection; affiliation partly naming-based. Maps to weeks 3;4. License metadata: NONE-DETECTED.

Entry point: `cs_dialogue_whisper_LoRA.ipynb`.

Read the notebook: 42 cells, 32 code cells; XLS-R/Wav2Vec2 CTC code, code-switching data, WER/CER and adapter tooling.

**Caution:** No readable README found. Filename says Whisper but its content identifies XLS-R-300M. Do not infer a Whisper implementation or official module from filename.

### NUS-AIS-Practice-Modules/CryptoPulse

https://github.com/NUS-AIS-Practice-Modules/CryptoPulse

Type: project implementation; exact course attribution unconfirmed. Maps to weeks 4;5;6;7. License metadata: NONE-DETECTED.

Entry point: `docs/INTERFACES.md`.

README and actual interface specification show FastAPI, hybrid retrieval, Milvus, BGE-M3 and a LoRA/vLLM bridge.

**Caution:** Same organisation is not proof of a specific course/intake. Requires local model caches, external data and remote GPU service; not a free one-command reproduction.

### IRS-PM/Workshop-Project-Submission-Template

https://github.com/IRS-PM/Workshop-Project-Submission-Template

Type: submission template and example, not a separate cohort result. Maps to weeks 7. License metadata: NONE-DETECTED.

Entry point: `README.md`.

Contains a project-submission structure, naming convention, sample BTO example and report/user-guide/code folders.

**Caution:** Do not count copied example text or placeholder student details as evidence of a new project or syllabus topic.

### IRS-PM/IRS-PM-2020-01-18-IS02PT-GRP2-Enterprise-Knowledge-Graph

https://github.com/IRS-PM/IRS-PM-2020-01-18-IS02PT-GRP2-Enterprise-Knowledge-Graph

Type: student project. Maps to weeks 5;7. License metadata: NONE-DETECTED.

Entry point: `ProjectReport/EKGS_Project Report_Group2.pdf`.

README describes enterprise graph exploration; tree includes backend/frontend, graph data and compose files.

**Caution:** A knowledge graph is not automatically RAG or an LLM system. Older stack; reports not independently reproduced.

### IRS-PM/IRS-PM-2023-08-21-GRP17-Album-Generator

https://github.com/IRS-PM/IRS-PM-2023-08-21-GRP17-Album-Generator

Type: student project. Maps to weeks 3;4;7. License metadata: NONE-DETECTED.

Entry point: `SystemCode/backend/album/layout_decision_maker/GA.py`.

README describes photo organisation; tree includes image recognition, deduplication and genetic layout code.

**Caution:** Album generation is not proof of diffusion image synthesis. Useful for systems decomposition, not a Stable Diffusion substitute.

### IRS-PM/IRS-PM-2023-08-21-GRP24-Academic-Knowledge-Platform

https://github.com/IRS-PM/IRS-PM-2023-08-21-GRP24-Academic-Knowledge-Platform

Type: student project. Maps to weeks 5;7. License metadata: NONE-DETECTED.

Entry point: `README.md`.

README describes paper search/summaries plus a recommender; report and demo links are present.

**Caution:** Search/recommendation does not by itself prove a modern RAG architecture. Demo videos were not transcribed in this pass.

### IRS-PM/IRS-PM-2023-08-21-GRP19-Rebalancing-Data-Research

https://github.com/IRS-PM/IRS-PM-2023-08-21-GRP19-Rebalancing-Data-Research

Type: student research project. Maps to weeks 2;3;4. License metadata: NONE-DETECTED.

Entry point: `main.py`.

README claims a generative rebalancing method for imbalanced partial labels; tree contains ResNet/model/loss code and report.

**Caution:** Reported improvements are authors claims, not reproduced benchmark evidence. Not a direct analogue of a short GenAI applications module.

### IRS-PM/IRS-PM-2023-08-21-GRP1-AbuseDetection

https://github.com/IRS-PM/IRS-PM-2023-08-21-GRP1-AbuseDetection

Type: student project. Maps to weeks 2;3;7. License metadata: NONE-DETECTED.

Entry point: `SystemCode/Abuse Text classification/Notebooks/Abuse Text classification - MLP Model.ipynb`.

README and notebook tree cover text/image classification, ML and DL comparisons.

**Caution:** Potentially offensive source datasets; not downloaded. Copied template footer is weak course attribution by itself.

### IRS-PM/IRS-PM-2023-03-06-ISY5001-GRP-Two.AI-ChattyISS

https://github.com/IRS-PM/IRS-PM-2023-03-06-ISY5001-GRP-Two.AI-ChattyISS

Type: student project. Maps to weeks 5;7. License metadata: NONE-DETECTED.

Entry point: `README.md`.

README identifies an ISS-information chatbot problem and code/report artifacts.

**Caution:** Large mixed repository includes documents and automation assets. Do not equate a chatbot label with a current LLM or trustworthy live information.

### IRS-PM/2023-05-25-Dog-Breed-Detective

https://github.com/IRS-PM/2023-05-25-Dog-Breed-Detective

Type: student project. Maps to weeks 3;7. License metadata: NONE-DETECTED.

Entry point: `Miscellaneous/CNN modelling/CNN_Transfer_Learning_Feature_Extraction.ipynb`.

Read actual TensorFlow/Keras feature-extraction notebook: ResNet50V2, DenseNet121 and NASNetMobile features feed a dense classifier.

**Caution:** Important audit issue: features are allocated into a uint8 array, risking loss of floating-point information. Reference the idea, not unquestioned code quality. Local image paths/weights are required.

### IRS-PM/IRS-PM-2021-01-16-IS03PT-GRP-HDB-Resale-Price-Recommender

https://github.com/IRS-PM/IRS-PM-2021-01-16-IS03PT-GRP-HDB-Resale-Price-Recommender

Type: student project. Maps to weeks 1;2;7. License metadata: NONE-DETECTED.

Entry point: `HDBResaleWeb/recommendation.py`.

README describes historical resale prediction/recommendation; tree includes data retrieval, feature helpers and web app.

**Caution:** Old domain data and scraping assumptions. Do not use historical prices as current estimates.

### IRS-PM/IRS-PM-2020-11-01-IS02FT-GRP11-NewsCurator

https://github.com/IRS-PM/IRS-PM-2020-11-01-IS02FT-GRP11-NewsCurator

Type: student project. Maps to weeks 1;5;7. License metadata: NONE-DETECTED.

Entry point: `app/business/process_news_articles.py`.

README and tree show personalised news processing and rule-based components.

**Caution:** Rule-based recommendation, not evidence that LLM agents were taught in that cohort. Old APIs may fail.

### anastasiapatricks/JobAId

https://github.com/anastasiapatricks/JobAId

Type: student practice-module implementation. Maps to weeks 5;6;7. License metadata: MIT.

Entry point: `agents/orchestrator.py`.

README explicitly states NUS-ISS Practice Module; inspected orchestrator transitions, job discovery and market-intelligence code.

**Caution:** Strong MIT-licensed fork base. Many claimed guardrails and explainability features still need independent testing; full external-service application not run.

### ISS-IS02PT/PRS-PM-ISY5002-GROUP5

https://github.com/ISS-IS02PT/PRS-PM-ISY5002-GROUP5

Type: student practice-module project. Maps to weeks 1;2;3;6;7. License metadata: GPL-3.0.

Entry point: `SystemCode/setup-streamlit/project-usecases/st-usecase1.py`.

README describes write-off classification, revenue forecasting and bill estimation; inspected serving code and notebook tree.

**Caution:** GPL-3.0 source, not copied into original lessons. Real healthcare data availability/permissions are unresolved. README footer contains reasoning-course names despite PRS content, showing template drift.

### atsui888/MTech-AI-Capstone-Project

https://github.com/atsui888/MTech-AI-Capstone-Project

Type: student capstone presentation. Maps to weeks 7. License metadata: NONE-DETECTED.

Entry point: `Project PPT/Cerebro Index Presentation v02.pdf`.

README explicitly names MTech AIS capstone and explains a question-complexity framework; presentation PDF is in tree.

**Caution:** Only four files in inspected tree; not a complete runnable training pipeline. Do not treat a presentation as reproducible source code.

### bleongcw/generativeai_course

https://github.com/bleongcw/generativeai_course

Type: instructor course material, self-described. Maps to weeks 3;4;5;7. License metadata: NONE-DETECTED.

Entry point: `nlp_transformers_embeddings/06_rag_evaluation_failure_modes_and_best_practices.ipynb`.

README maps prompt/tool/agent/embedding/RAG lessons; inspected 12-cell RAG-evaluation notebook with mock-safe paths.

**Caution:** Best modern lesson sequence found, but no repository-wide license detected. Link for study; do not bulk copy. NUS-ISS material is not exact SCTP SoC material.

### bleongcw/archaas-nus-iss-workshop1

https://github.com/bleongcw/archaas-nus-iss-workshop1

Type: instructor workshop, self-described. Maps to weeks 4;5. License metadata: NONE-DETECTED.

Entry point: `individual_assignment_day1.ipynb`.

README explicitly identifies ARCHAAS Day 1 and lists prompt, agent, Bedrock, reasoning and assignment notebooks.

**Caution:** Not a student submission. No repository-wide license detected; paid provider calls may exist in optional labs.

### IRS-MR/S-MR-Workshop

https://github.com/IRS-MR/S-MR-Workshop

Type: teaching workshop and project guidance. Maps to weeks 5;7. License metadata: NOASSERTION.

Entry point: `README.md`.

Explicit NUS-ISS Machine Reasoning/IRS context and workshop project guidance.

**Caution:** Older symbolic reasoning emphasis. License is nonstandard/NOASSERTION in API metadata; inspect terms before reuse.

### aaxwaz/NUS_ISS_DeepLearningWorkshop

https://github.com/aaxwaz/NUS_ISS_DeepLearningWorkshop

Type: teaching workshop, self-described. Maps to weeks 3. License metadata: NONE-DETECTED.

Entry point: `HandsOn/catsanddogs_tutorial.ipynb`.

README identifies a NUS-ISS computer-vision masterclass; slide decks and hands-on image notebooks appear in tree.

**Caution:** No repository-wide license detected; large tree includes dataset assets. No claim that all assets are owned by the uploader or current.

### bhuiyanmobasshir94/NUS-Artificial-Intelligence-Training

https://github.com/bhuiyanmobasshir94/NUS-Artificial-Intelligence-Training

Type: participant training archive, self-described. Maps to weeks 1;2;3. License metadata: MIT.

Entry point: `Sessions/SESSION_2/WORKSHOPS/S2 knn-logreg-NB.ipynb`.

Read 50-cell notebook with train/test split, StandardScaler, logistic regression, confusion matrix and ROC; session tree has classical ML and DL workshops.

**Caution:** Different 2020 IT/ITES training programme, not SCTP AIE. MIT repository metadata does not settle rights in third-party slide decks and datasets.

### danieltanhx/IRS-PM-2020-01-18-IS02PT-GRP7-Smart-Job-Recommender-System

https://github.com/danieltanhx/IRS-PM-2020-01-18-IS02PT-GRP7-Smart-Job-Recommender-System

Type: student project. Maps to weeks 1;2;5;7. License metadata: MIT.

Entry point: `SystemCode/Data Mining/code/Machine Learning.py`.

README and tree show web collection, data preparation, model notebooks and rule-engine integration.

**Caution:** MIT code base but old APIs and scraped job data; not a modern LLM curriculum or permission to re-publish job data.

## How much can really be reconstructed?

The topic map is high confidence because the seven official module pages name their objectives. The exact teaching sequence, tool versions, dataset choices, assessment difficulty and assignment rubrics are low confidence because the private teaching materials were not recovered. The proposed order is pedagogically motivated: data before models, validation before deep learning, mechanisms before generative applications, retrieval before agent orchestration, and operations before the final project. This is a useful independent course, not a copy of the paid programme.

## Assessment and portfolio

Use the original 100-point rubric in each repo: reproducibility/tests 25, correct mechanism/explanation 25, evaluation 20, failures/provenance/limits 20, communication 10. Suggested pass 70 with no fabricated results or private-data exposure. These are self-study weights, not NUS marking weights.

By week seven, maintain a dataset card, model card, evaluation report, demo script, runbook and a command log. Show one successful path and at least two failures. A synthetic educational demo is not ready to make decisions about actual learners.

## Hardware, cost and mobile use

Core notebooks use marimo, NumPy, pandas and standard-library code. They run in a browser using WebAssembly, with an initial runtime/package download. Native deeper labs add sklearn, CPU PyTorch or LangGraph. There are no default API calls, remote inference, model-weight downloads, cloud resources or paid subscriptions. Upstream JobAId/WhatsEat live integrations can need credentials and billable services; they are not automatically run. The GitHub Pages notebooks are free static hosting, not a server-side model API.

A phone can read the snapshots and run the small browser labs where its browser supports the runtime. The deeper training notebooks are local desktop work. Large training jobs, pretrained image models, browser memory pressure and download time remain practical limits.

## Known gaps and next work

1. No exact-programme student assignments or official assessment rubric were recovered in this pass.
2. The default course does not run pretrained BERT/GPT/Stable Diffusion or real multimodal foundation models. Those named official families need a separate opt-in model-card/hardware/license review.
3. Student repositories may contain defects, stale APIs, incomplete reports and third-party data. Public visibility is not a blanket license.
4. The original fork application has not been fully executed, penetration-tested or dependency-audited. Only selected relevant implementation paths were inspected.
5. Browser compatibility is verified through the recorded viewport/runtime checks, not a guarantee for every phone or in-app browser. Static snapshots are the fallback.
6. The seven-week allocation is an original 106-hour estimate. It does not imply equivalent accreditation or employment readiness.

## Verification record

See the per-repository TEST_RESULTS.txt and verification summary in the delivery bundle. Static export success alone is not treated as visual or interaction verification. The final delivery includes only the checked publication state.

## Official programme anchor

https://www.comp.nus.edu.sg/executive-education/sctp/nus-ai-engineering-programme/

## Method

Search public web sources; verify official objectives; retrieve repository metadata, complete file trees and relevant README excerpts; inspect selected actual code/notebook cells; classify templates/forks separately; check licensing; map evidence to objectives; design original lessons; execute and test; inspect visual output and interactions; publish only the checked result. No LMS access, private-course scraping, credentials or student personal details are included in this report.

## Published learning sites

- Week 1: https://azjhf-dev.github.io/nus-aie-week-01-python/ | source: https://github.com/azjhf-dev/nus-aie-week-01-python
- Week 2: https://azjhf-dev.github.io/nus-aie-week-02-machine-learning/ | source: https://github.com/azjhf-dev/nus-aie-week-02-machine-learning
- Week 3: https://azjhf-dev.github.io/nus-aie-week-03-deep-learning/ | source: https://github.com/azjhf-dev/nus-aie-week-03-deep-learning
- Week 4: https://azjhf-dev.github.io/nus-aie-week-04-generative-ai/ | source: https://github.com/azjhf-dev/nus-aie-week-04-generative-ai
- Week 5: https://azjhf-dev.github.io/nus-aie-week-05-llm-agents/ | source: https://github.com/azjhf-dev/nus-aie-week-05-llm-agents
- Week 6: https://azjhf-dev.github.io/nus-aie-week-06-mlops/ | source: https://github.com/azjhf-dev/nus-aie-week-06-mlops
- Week 7: https://azjhf-dev.github.io/nus-aie-week-07-capstone/ | source: https://github.com/azjhf-dev/nus-aie-week-07-capstone

# Verification of the independent learning build

Checked 19 November 2026.

- Seven separate repositories; week 5 is a genuine JobAId fork with the MIT notice preserved.
- Fourteen Marimo notebooks executed successfully to HTML: seven mechanism labs and seven deeper project labs.
- 133 deterministic tests passed across the learning_tests directories. These are 17 shared numerical/validation tests per repo plus module-specific tests, not 133 distinct topic objectives.
- Actual CNN, RNN and Transformer training checked on synthetic held-out tasks. Actual VAE, 2D DDPM and masked/causal objective training checked for finite outputs and learning. These are not pretrained-model benchmarks.
- Actual LangGraph review rejection/resume checked. Actual local HTTP health/prediction/invalid-input checks passed.
- Every published core browser notebook loaded, a slider value was changed, output text changed, and its conceptual animation paused. No browser script errors were observed in those checks.
- All fourteen read-only snapshots were visually inspected at 390px width. Core live views were also captured at 320px and 1280px. Tables can scroll horizontally. The static export warns that its controls cannot rerun Python; use the interactive core link or run locally.
- Landing-page links and publication state were checked without sign-in.

## Limits

This is not a full audit of inherited JobAId code, upstream dependency security, all devices, private NUS assessments or a production deployment. Static pages do not provide a server-side inference API. Browser runtime downloads need internet and can be slow or memory-limited on phones. No keys, private data, paid APIs or compute purchases are needed for the supplied default lessons.
