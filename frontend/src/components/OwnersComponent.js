// src/components/OwnersComponent.js
import React, { useEffect, useState } from 'react';
import { fetchOwners } from '../api/ownersApi'; // Adjust the path as necessary
import './OwnersComponent.css'; // Import the CSS file for styling

const OwnersComponent = () => {
    const [owners, setOwners] = useState([]); // State for owners
    const [loading, setLoading] = useState(true); // Loading state

    useEffect(() => {
        const loadOwners = async () => {
            try {
                const ownersData = await fetchOwners(); // Call fetchOwners to get owners
                setOwners(ownersData); // Update state with fetched owners
            } catch (error) {
                console.error('Failed to load owners:', error);
            } finally {
                setLoading(false); // Set loading to false after fetching
            }
        };

        loadOwners(); // Trigger the fetching of owners
    }, []); // Empty dependency array to run on mount

    if (loading) {
        return <div className="loading">Loading...</div>; // Display loading message
    }

    return (
        <div className="owners-container">
            <h1>Owners</h1>
            <table className="owners-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Contact Email</th>
                        <th>Contact Number</th>
                    </tr>
                </thead>
                <tbody>
                    {owners.map((owner) => (
                        <tr key={owner.id}>
                            <td>{owner.id}</td>
                            <td>{owner.contact_email}</td>
                            <td>{owner.contact_number}</td> {/* Adjust this field as necessary */}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default OwnersComponent;
