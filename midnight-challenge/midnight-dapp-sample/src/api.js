export async function sendTx(data) {
  const res = await fetch("http://localhost:4000/midnight/tx", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getBalance(address) {
  const res = await fetch(`http://localhost:5000/midnight/balance/${address}`);
  return res.json();
}
