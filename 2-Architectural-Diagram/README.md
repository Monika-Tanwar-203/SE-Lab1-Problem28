# Architectural Diagram – Problem Statement 28

## Inter-City Freight Load Matching Marketplace

### System Architecture

```mermaid
flowchart LR

    S[Shipper] --> UI[Web / Mobile Interface]
    C[Freight Carrier] --> UI
    A[Admin] --> UI

    UI --> AUTH[Authentication & User Management]
    UI --> LOAD[Load Posting & Management]
    UI --> MATCH[Load Matching & Bidding]
    UI --> VERIFY[Carrier Verification & Permit Management]
    UI --> TRACK[Shipment Tracking]
    UI --> PAY[Payment & Escrow Management]

    AUTH --> DB[(Database)]
    LOAD --> DB
    MATCH --> DB
    VERIFY --> DB
    TRACK --> DB
    PAY --> DB

    TRACK --> GPS[GPS / Location Service]
    PAY --> GATEWAY[Payment Gateway]

    MATCH --> NOTIFY[Notification Service]
    TRACK --> NOTIFY
    PAY --> NOTIFY

    NOTIFY --> S
    NOTIFY --> C

    TRACK --> POD[Proof of Delivery]
    POD --> PAY
