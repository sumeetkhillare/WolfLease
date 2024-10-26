// src/components/ApartmentsComponent.js
import React, { useEffect, useState } from 'react';
import { fetchApartments } from '../api/apartmentsApi';
import './ApartmentsComponent.css';

const ApartmentsComponent = () => {
    const [apartments, setApartments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadApartments = async () => {
            try {
                const apartmentData = await fetchApartments();
                setApartments(apartmentData);
            } catch (error) {
                console.error('Failed to load apartment:', error);
            } finally {
                setLoading(false);
            }
        };

        loadApartments();
    }, []);

    if (loading) {
        return <div className="loading">Loading...</div>;
    }

    return (
        <div className="apartments-container">
            <h1>Apartments</h1>
            <table className="apartments-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Address</th>
                        <th>Facilities</th>
                        <th>Owner Id</th>
                    </tr>
                </thead>
                <tbody>
                    {apartments.map((apartment) => (
                        <tr key={apartment.id}>
                            <td>{apartment.id}</td>
                            <td>{apartment.address}</td>
                            <td>{apartment.facilities}</td>
                            <td>{apartment.owner_id}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ApartmentsComponent;
