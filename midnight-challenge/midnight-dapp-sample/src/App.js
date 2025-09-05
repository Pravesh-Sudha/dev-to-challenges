import React, { useState } from "react";
import { sendTx, getBalance } from "./api";

function App() {
  const [address, setAddress] = useState("user1");
  const [balance, setBalance] = useState(null);
  const [txHash, setTxHash] = useState("");

  const handleSendTx = async () => {
    const res = await sendTx({ from: address, to: "user2", amount: 10 });
    setTxHash(res.tx_hash);
  };

  const handleGetBalance = async () => {
    const res = await getBalance(address);
    setBalance(res.balance);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>🌙 Midnight dApp Sample</h1>

      <div style={styles.card}>
        <h2 style={styles.sectionTitle}>Wallet</h2>
        <input
          type="text"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          style={styles.input}
          placeholder="Enter your address"
        />
        <button style={styles.button} onClick={handleGetBalance}>
          Get Balance
        </button>
        {balance !== null && <p style={styles.result}>Balance: {balance}</p>}
      </div>

      <div style={styles.card}>
        <h2 style={styles.sectionTitle}>Transaction</h2>
        <button style={styles.button} onClick={handleSendTx}>
          Get Transaction
        </button>
        {txHash && <p style={styles.result}>Tx Hash: {txHash}</p>}
      </div>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "Arial, sans-serif",
    background: "#0f172a",
    color: "#e2e8f0",
    minHeight: "100vh",
    padding: "2rem",
    textAlign: "center",
  },
  header: {
    fontSize: "2.2rem",
    marginBottom: "2rem",
    color: "#38bdf8",
  },
  card: {
    background: "#1e293b",
    padding: "1.5rem",
    margin: "1rem auto",
    borderRadius: "12px",
    maxWidth: "400px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
  },
  sectionTitle: {
    fontSize: "1.3rem",
    marginBottom: "1rem",
    color: "#f8fafc",
  },
  input: {
    padding: "0.6rem",
    width: "100%",
    borderRadius: "8px",
    border: "1px solid #334155",
    marginBottom: "1rem",
    background: "#0f172a",
    color: "#f8fafc",
  },
  button: {
    background: "#38bdf8",
    color: "#0f172a",
    padding: "0.7rem 1.2rem",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
    marginTop: "0.5rem",
  },
  result: {
    marginTop: "1rem",
    fontSize: "1rem",
    color: "#a5f3fc",
  },
};

export default App;
