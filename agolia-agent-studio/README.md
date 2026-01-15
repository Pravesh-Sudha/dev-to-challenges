# Terraform to Product Impact

### Explaining AWS Infrastructure to Product Managers using Algolia Agent Studio

This project demonstrates a **non-conversational AI agent** built with **Algolia Agent Studio** that translates **AWS infrastructure defined using Terraform** into **clear, Product Manager–friendly explanations**.

The agent focuses on **what the infrastructure does and why it matters**, rather than how it is implemented. It helps bridge the communication gap between engineering teams and non-technical stakeholders by turning Terraform summaries into structured, business-focused system overviews.


## Problem Statement

Infrastructure is typically written for engineers. Even when summaries exist, they often assume deep AWS or Terraform knowledge.

Product Managers, however, need to understand:

* how users access the system,
* where data is stored,
* how the system scales,
* and what operational or cost risks exist,

without reading Terraform code or AWS documentation.

**Infrastructure doesn’t fail because it’s complex — it fails because the right people don’t understand it at the right time.**

This project addresses that gap.


## What This Project Does

* Accepts a **Terraform infrastructure summary** as input
* Uses **Algolia Agent Studio** to retrieve relevant AWS context
* Produces a **PM-level system explanation** describing:

  * system overview
  * user access patterns
  * data and storage
  * operational considerations

The agent is intentionally scoped to **AWS + Terraform** and avoids low-level implementation details.


## Project Structure

```text
agolia-agent-studio/
├── doc/
│   ├── prompt.txt
│   └── summaries.txt
├── index/
│   └── records.json
```

### Directory Overview

* **`doc/prompt.txt`**
  Contains the full agent prompt used in Algolia Agent Studio, defining scope, tone, behavior, and output structure.

* **`doc/summaries.txt`**
  Contains sample Terraform infrastructure summaries used to test and demonstrate the agent.

* **`index/records.json`**
  Contains the structured records uploaded to the Algolia index.
  Each record represents a PM-friendly explanation of an AWS service or Terraform resource.

## Indexed Services

The Algolia index contains **13 curated AWS services**, chosen to maximize signal and avoid hallucination:

* Amazon EKS
* Amazon ECS
* Amazon EC2
* AWS Lambda
* Amazon API Gateway
* Elastic Load Balancer
* Amazon RDS
* Amazon S3
* Amazon CloudFront
* Amazon CloudWatch
* AWS Identity and Access Management (IAM)
* Amazon VPC
* AWS Billing & Cost Management (conceptual)

Each service includes a **Product Manager–focused explanation**, not Terraform or AWS configuration details.

## How Algolia Agent Studio Is Used

1. An index named `terra-pr` is created in Algolia Agent Studio.
2. The `records.json` file is uploaded to populate the index.
3. A new agent is created from scratch.
4. Gemini is configured as the LLM provider.
5. The `terra-pr` index is added to the agent as a retrieval tool.
6. A targeted prompt guides the agent to:

   * use retrieved context only,
   * explain infrastructure for a Product Manager audience,
   * compose a coherent system-level explanation.

Fast retrieval ensures the agent remains accurate, consistent, and grounded in known context.

## Example Usage

Input (Terraform Summary):

```
This infrastructure provisions an AWS EKS cluster to run containerized application workloads.
User traffic enters through a load balancer, data is stored in RDS and S3, and monitoring is handled by CloudWatch.
```

Output:

A structured, PM-level explanation describing:

* how the system operates,
* how users interact with it,
* where data lives,
* and what operational considerations exist.

No Terraform syntax is exposed.

## Why This Approach Works

* Retrieval limits hallucination
* Curated index keeps explanations focused
* Opinionated scope improves clarity
* Outputs are consistent and repeatable

Even when infrastructure summaries exist, they are written for engineers.
**This agent ensures every infrastructure change can be understood by a Product Manager in minutes.**

## Technologies Used

* Algolia Agent Studio
* Algolia Search Index
* Gemini (LLM provider)
* Terraform (infrastructure context)
* AWS (target cloud platform)

## Author

**Pravesh Sudha**

* LinkedIn: [https://www.linkedin.com/in/pravesh-sudha/](https://www.linkedin.com/in/pravesh-sudha/)
* Twitter / X: [https://x.com/praveshstwt](https://x.com/praveshstwt)
* YouTube: [https://www.youtube.com/@pravesh-sudha](https://www.youtube.com/@pravesh-sudha)
* Blog: [https://blog.praveshsudha.com](https://blog.praveshsudha.com)
