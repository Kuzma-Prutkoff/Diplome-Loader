import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../styles/InfoPanel.css";
import { GROUPS, SWAGGER_URL } from "../utils/constants.js";
import MainInfo from "./MainInfo.jsx";
import serviceContext from "../context/createContext.js";

const InfoPanel = () => {
  const { pageId, setPageId } = useContext(serviceContext);
  const [userName, setUserName] = useState(localStorage.getItem("user"));
  const [group, setGroup] = useState(localStorage.getItem("group"));
  const [title, setTitle] = useState(" ");

  useEffect(() => {
    if (pageId === 1) {
      setTitle(
        "Информация о комплектациях и технических характеристиках Вашей техники"
      );
    } else if (pageId === 2) {
      setTitle("Информация о техническом обслуживании Вашей техники");
    } else if (pageId === 3) {
      setTitle("Информация о рекламациях Вашей техники");
    }
  }, [pageId]);

  return (
    <div className="info-panel">
      <h2 className="main-user-info">
        {GROUPS[group]}: {userName}
      </h2>
      <div className="title-container">
        <h1 className="info-panel-title">{title}</h1>
        {group === "3" && (
          <div className="swagger-container">
            <Link className="catalog-link" to={"/catalogs"}>
              Справочники
            </Link>
            <a className="swagger-link" href={SWAGGER_URL} target="_blank">
              API-Инструкция
            </a>
          </div>
        )}
      </div>
      <MainInfo />
    </div>
  );
};

export default InfoPanel;
