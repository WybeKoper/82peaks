import React, { useState } from "react";
import Datepicker from "react-tailwindcss-datepicker";

const Picker = () => {
  const [value, setValue] = useState({
    startDate: null,
    endDate: null,
  });

  const handleValueChange = (newValue) => {
    console.log("newValue:", newValue);
    setValue(newValue);
  };

  return (
    <Datepicker
      primaryColor={"sky"}
      value={value}
      onChange={handleValueChange}
      showShortcuts={true}
      data-theme="light"
    />
  );
};
export default Picker;
