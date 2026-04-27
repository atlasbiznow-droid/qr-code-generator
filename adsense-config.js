/**
 * AdSense Configuration for ABN Free QR Code Generator
 * 
 * Instructions:
 * 1. Go to https://adsense.google.com and create an account
 * 2. Get your publisher ID (format: pub-xxxxxxxxxxxxxxx)
 * 3. Replace 'YOUR_PUBLISHER_ID' below with your actual publisher ID
 * 4. Create ad units in AdSense and get your ad client IDs
 */

const AdSenseConfig = {
    // Your Google AdSense Publisher ID
    publisherId: 'YOUR_PUBLISHER_ID',
    
    // Ad Unit IDs for different placements
    adUnits: {
        // Top leaderboard (typically 728x90 or responsive)
        leaderboard: {
            adClient: 'ca-pub-YOUR_PUBLISHER_ID',
            adSlot: 'YOUR_AD_SLOT_ID_1'
        },
        
        // Sidebar (typically 300x250)
        sidebar: {
            adClient: 'ca-pub-YOUR_PUBLISHER_ID',
            adSlot: 'YOUR_AD_SLOT_ID_2'
        },
        
        // In-content (typically 300x250 or responsive)
        inContent: {
            adClient: 'ca-pub-YOUR_PUBLISHER_ID',
            adSlot: 'YOUR_AD_SLOT_ID_3'
        }
    },
    
    // Enable/disable ads (set to false for development)
    enabled: false,
    
    // Test mode - shows test ads (set to true initially)
    testMode: true
};

// Auto-ad.js script loader
(function loadAdSense() {
    if (!AdSenseConfig.enabled && !AdSenseConfig.testMode) {
        console.log('Ads disabled in config');
        return;
    }
    
    const script = document.createElement('script');
    script.src = `https://pagead2.googlesyndication.com/pagead/show.js?client=ca-pub-${AdSenseConfig.publisherId}`;
    script.async = true;
    document.head.appendChild(script);
})();

console.log('AdSense config loaded. Update adsense-config.js with your publisher ID.');