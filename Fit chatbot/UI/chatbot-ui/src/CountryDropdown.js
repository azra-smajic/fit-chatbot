import React from 'react';
import Select from 'react-select';
import 'flag-icons/css/flag-icons.min.css';

const countries = [
    { value: 'en', label: 'United Kingdom', flag: 'gb' },
    { value: 'hr', label: 'Croatia', flag: 'hr' },
    { value: 'bs', label: 'Bosnia and Herzegovina', flag: 'ba' }
];

const customSingleValue = ({ data }) => (
    <div style={{ display: 'flex', alignItems: 'center' }}>
        <span className={`fi fi-${data.flag}`} style={{ marginRight: 10 }}></span>
        {data.label}
    </div>
);

const customOption = (props) => {
    const { innerRef, innerProps, data } = props;
    return (
        <div ref={innerRef} {...innerProps} style={{ display: 'flex', alignItems: 'center' }}>
            <span className={`fi fi-${data.flag}`} style={{ marginRight: 10 }}></span>
            {data.label}
        </div>
    );
};

const CountryDropdown = ({ onChange }) => {
    return (
        <Select
            options={countries}
            getOptionLabel={(option) => (
                <div style={{ display: 'flex', alignItems: 'center' }}>
                    <span className={`fi fi-${option.flag}`} style={{ marginRight: 10 }}></span>
                    {option.label}
                </div>
            )}
            getOptionValue={(option) => option.value}
            components={{ SingleValue: customSingleValue, Option: customOption }}
            onChange={(selectedOption) => onChange(selectedOption.value)}
            placeholder="Select country..."
        />
    );
};

export default CountryDropdown;