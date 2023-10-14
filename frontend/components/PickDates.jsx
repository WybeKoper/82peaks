import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const PickDates = () => {
  const [dateRange, setDateRange] = useState([null, null]);
  const [startDate, endDate] = dateRange;
  const today = new Date();
  const tomorrow = new Date();
  const latestDate = new Date();
  tomorrow.setDate(today.getDate() + 1);
  latestDate.setDate(today.getDate() + 5);

  const [mountain, setMountain] = useState([]);

  const fetchMountain = async () => {
    if (!(startDate == null || endDate == null)) {
      const response = await fetch(
        "api/bestweather" +
          "?" +
          "startDate=" +
          startDate.toISOString().split("T")[0] +
          "&" +
          "endDate=" +
          endDate.toISOString().split("T")[0]
      );
      const data = await response.json();
      setMountain(data);
    }
  };

  return (
    <div>
      <div className="flex items-center justify-center">
        <div>
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
        </div>
        <div className="pl-5">
          <button
            className="bg-slate-200  p-1 border rounded border-gray-800 hover:bg-slate-500"
            onClick={fetchMountain}
          >
            Find Peak
          </button>
        </div>
      </div>
      <div>
        {mountain.map((mont) => {
          return (
            <div className="flex items-center justify-center">
              <div className="p-1">{mont.mountain_name}</div>
              <div className="p-1">
                <a href={mont.url}>Detailed Forecast</a>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PickDates;
