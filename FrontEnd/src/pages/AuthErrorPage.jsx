import React from "react";
import "../styles/AuthErrorPage.css";
import { useNavigate } from "react-router-dom";

const AuthErrorPage = () => {
  const navigate = useNavigate();

  const handleReturn = () => {
    navigate("/auth");
  };

  return (
    <div className="auth-error">
      <h1 className="auth-error-title">Ошибка авторизации.</h1>
      <div className="auth-error-content">
        Вы ввели неправильно пароль или логин. Повторите ввод.
      </div>
      <button className="auth-error-btn" onClick={handleReturn}>
        Вернуться
      </button>
    </div>
  );
};

export default AuthErrorPage;
