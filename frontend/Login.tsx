import { useState } from "react";
import axios from "axios";

export default function Login() {
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const [step, setStep] = useState(1);

  const requestCode = async () => {
    await axios.post("http://localhost:8000/auth/request-code", { email });
    setStep(2);
  };

  const verifyCode = async () => {
    const res = await axios.post("http://localhost:8000/auth/verify", { email, code });
    localStorage.setItem("token", res.data.access_token);
    alert("Login successful");
  };

  return (
    <div className="flex flex-col gap-4 max-w-sm mx-auto mt-20">
      <h2 className="text-xl font-bold text-center">Login</h2>
      {step === 1 ? (
        <>
          <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter your email" className="p-2 border rounded" />
          <button onClick={requestCode} className="p-2 bg-black text-white rounded">Request Code</button>
        </>
      ) : (
        <>
          <input value={code} onChange={e => setCode(e.target.value)} placeholder="Enter code" className="p-2 border rounded" />
          <button onClick={verifyCode} className="p-2 bg-black text-white rounded">Verify</button>
        </>
      )}
    </div>
  );
}