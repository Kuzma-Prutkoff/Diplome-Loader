import React, { useState, useRef } from "react";
import "../styles/MainInfo.css";
import MainBlock from "./MainBlock.jsx";
import MaintenanceBlock from "./MaintenanceBlock.jsx";
import ComplaintBlock from "./ComplaintBlock.jsx";

const MainInfo = () => {
  const [currentDataType, setCurrentDataType] = useState(1);
  const [currentGroup, setCurrentGroup] = useState(
    localStorage.getItem("group")
  );
  const mainRef = useRef();
  const maintenanceRef = useRef();
  const complaintRef = useRef();

  const handleMainInfo = () => {
    mainRef.current.className = "nav-btn active";
    maintenanceRef.current.className = "nav-btn passive";
    complaintRef.current.className = "nav-btn passive";
    setCurrentDataType(1);
  };

  const handleMaintenanceInfo = () => {
    mainRef.current.className = "nav-btn passive";
    maintenanceRef.current.className = "nav-btn active";
    complaintRef.current.className = "nav-btn passive";
    setCurrentDataType(2);
  };

  const handleComplaintInfo = () => {
    mainRef.current.className = "nav-btn passive";
    maintenanceRef.current.className = "nav-btn passive";
    complaintRef.current.className = "nav-btn active";
    setCurrentDataType(3);
  };

  return (
    <div className="main-info">
      <div className="navigation-bar">
        <button
          ref={mainRef}
          onClick={handleMainInfo}
          className="nav-btn active"
        >
          Общая информация
        </button>
        <button
          ref={maintenanceRef}
          onClick={handleMaintenanceInfo}
          className="nav-btn passive"
        >
          ТО
        </button>
        <button
          ref={complaintRef}
          onClick={handleComplaintInfo}
          className="nav-btn passive"
        >
          Рекламации
        </button>
      </div>
      {currentDataType === 1 && <MainBlock group={currentGroup} />}
      {currentDataType === 2 && <MaintenanceBlock group={currentGroup} />}
      {currentDataType === 3 && <ComplaintBlock group={currentGroup} />}
    </div>
  );
};

export default MainInfo;
