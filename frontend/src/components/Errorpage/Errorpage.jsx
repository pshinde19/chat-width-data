import React from 'react';
import styles from './Errorpage.module.css';

const ErrorPage = ({ 
  errorCode = '404', 
  title = 'Page Not Found',
  message = 'Sorry, the page you are looking for does not exist or has been moved.',
  onGoHome 
}) => {
  const handleGoHome = () => {
    if (onGoHome) {
      onGoHome();
    } else {
      window.location.href = '/';
    }
  };

  return (
    <div className={styles.errorContainer}>
      <div className={styles.errorContent}>
        <div className={styles.glitchWrapper}>
          <div className={styles.errorCode} data-text={errorCode}>
            {errorCode}
          </div>
        </div>
        
        <h1 className={styles.errorTitle}>{title}</h1>
        <p className={styles.errorMessage}>{message}</p>
        
        <div className={styles.buttonGroup}>
          <button className={styles.primaryButton} onClick={handleGoHome}>
            <svg className={styles.icon} viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            Go Home
          </button>
          <button className={styles.secondaryButton} onClick={() => window.history.back()}>
            <svg className={styles.icon} viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Go Back
          </button>
        </div>
        
        <div className={styles.decoration}>
          <div className={styles.circle}></div>
          <div className={styles.circle}></div>
          <div className={styles.circle}></div>
        </div>
      </div>
    </div>
  );
};

export default ErrorPage;