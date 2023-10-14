import React, { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";


const Picker = () => {
  const [dateRange, setDateRange] = useState([null, null]);
  const [startDate, endDate] = dateRange;
  const today = new Date();
  const tomorrow = new Date()
  const latestDate = new Date()
  tomorrow.setDate(today.getDate() + 1)
  latestDate.setDate(today.getDate() + 5)
  return (
    <DatePicker
      className="p-1 bg-slate-200 border rounded border-gray-800"
      selectsRange={true}
      minDate={tomorrow}
      maxDate={latestDate}
      startDate={startDate}
      endDate={endDate}
      onChange={(update) => {
        setDateRange(update);
      }}
      placeholderText="When do you want to climb?"
      isClearable={true}
    />
  );
};
export default Picker;
