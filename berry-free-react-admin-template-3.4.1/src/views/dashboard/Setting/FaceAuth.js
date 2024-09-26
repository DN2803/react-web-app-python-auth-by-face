import React, { useState, useRef } from 'react';
import { Grid, Fab } from '@mui/material';
import { AddAPhoto } from '@mui/icons-material';
// project imports
import SubCard from 'ui-component/cards/SubCard';
import MainCard from 'ui-component/cards/MainCard';
import SecondaryAction from 'ui-component/cards/CardSecondaryAction';
import { gridSpacing } from 'store/constant';

// ==============================|| TYPOGRAPHY ||============================== //

const FaceAuth = () => {
    const [cameraActive, setCameraActive] = useState(false);
    const videoRef = useRef(null);

    const openCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            if (videoRef.current) {
                videoRef.current.srcObject = stream;
                videoRef.current.play(); // Start video playback
            }
            setCameraActive(true); // Show the video element
        } catch (err) {
            console.error("Error accessing the camera: ", err);
            alert('Unable to access the camera. Please check your permissions.');
        }
    };

    return (
        <>
            <MainCard title="Setting" secondary={<SecondaryAction link="https://next.material-ui.com/system/typography/" />}>
                <Grid container spacing={gridSpacing}>
                    <SubCard title="Create face authentication">
                        <Fab size="small" color="secondary" aria-label="add" onClick={openCamera}>
                            <AddAPhoto />
                        </Fab>
                        {cameraActive && (
                            <div style={{ marginTop: '20px' }}>
                                <video
                                    ref={videoRef}
                                    width="320"
                                    height="240"
                                    style={{ border: '1px solid black' }}
                                    autoPlay
                                    playsInline // Helps prevent issues on mobile devices
                                >
                                    {/* Add empty track for accessibility */}
                                    <track kind="captions" />
                                </video>
                            </div>
                        )}
                    </SubCard>
                </Grid>
            </MainCard>
        </>
    );
};

export default FaceAuth;
