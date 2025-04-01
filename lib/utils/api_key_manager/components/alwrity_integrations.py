"""ALwrity integrations setup component."""

import streamlit as st
from loguru import logger
from typing import Dict, Any
from ..manager import APIKeyManager
from .base import render_navigation_buttons, render_step_indicator, render_tab_style

def render_alwrity_integrations(api_key_manager: APIKeyManager) -> Dict[str, Any]:
    """Render the ALwrity integrations setup step."""
    try:
        # Apply enhanced tab styling
        render_tab_style()

        st.markdown("""
            <div class='setup-header'>
                <h2>🔄 ALwrity Integrations</h2>
                <p>Connect your content platforms and tools</p>
            </div>
        """, unsafe_allow_html=True)

        # Create tabs for different integration types
        tabs = st.tabs(["Website Platforms", "Social Media", "Analytics Tools"])

        changes_made = False
        has_valid_integrations = False
        validation_message = ""

        with tabs[0]:
            st.markdown("""
                <div class="tab-content">
                    <h3>Website Platforms</h3>
                    <p>Connect your website platforms for seamless content publishing</p>
                </div>
            """, unsafe_allow_html=True)

            # Website Platforms Grid
            col1, col2 = st.columns(2)

            with col1:
                # WordPress Card (Coming Soon)
                with st.container():
                    st.markdown("""
                        <div class="integration-card disabled">
                            <div class="integration-header">
                                <div class="integration-icon">🌐</div>
                                <div class="integration-title">WordPress <span class="coming-soon-badge">Coming Soon</span></div>
                            </div>
                            <div class="integration-content">
                                <p>Connect your WordPress site for direct content publishing.</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.info("WordPress integration will be available in the next update")

            with col2:
                # Wix Card (Coming Soon)
                with st.container():
                    st.markdown("""
                        <div class="integration-card disabled">
                            <div class="integration-header">
                                <div class="integration-icon">🎨</div>
                                <div class="integration-title">Wix <span class="coming-soon-badge">Coming Soon</span></div>
                            </div>
                            <div class="integration-content">
                                <p>Connect your Wix site for direct content publishing.</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.info("Wix integration will be available in the next update")

        with tabs[1]:
            st.markdown("""
                <div class="tab-content">
                    <h3>Social Media</h3>
                    <p>Connect your social media accounts for content distribution</p>
                </div>
            """, unsafe_allow_html=True)

            # Social Media Grid
            col1, col2 = st.columns(2)

            with col1:
                # Facebook Card (Coming Soon)
                with st.container():
                    st.markdown("""
                        <div class="integration-card disabled">
                            <div class="integration-header">
                                <div class="integration-icon">📘</div>
                                <div class="integration-title">Facebook <span class="coming-soon-badge">Coming Soon</span></div>
                            </div>
                            <div class="integration-content">
                                <p>Connect your Facebook account for content sharing.</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.info("Facebook integration will be available in the next update")

            with col2:
                # Instagram Card (Coming Soon)
                with st.container():
                    st.markdown("""
                        <div class="integration-card disabled">
                            <div class="integration-header">
                                <div class="integration-icon">📸</div>
                                <div class="integration-title">Instagram <span class="coming-soon-badge">Coming Soon</span></div>
                            </div>
                            <div class="integration-content">
                                <p>Connect your Instagram account for content sharing.</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.info("Instagram integration will be available in the next update")

        with tabs[2]:
            st.markdown("""
                <div class="tab-content">
                    <h3>Analytics Tools</h3>
                    <p>Connect your analytics tools for content performance tracking</p>
                </div>
            """, unsafe_allow_html=True)

            # Google Search Console Card (Coming Soon)
            with st.container():
                st.markdown("""
                    <div class="integration-card disabled">
                        <div class="integration-header">
                            <div class="integration-icon">📊</div>
                            <div class="integration-title">Google Search Console <span class="coming-soon-badge">Coming Soon</span></div>
                        </div>
                        <div class="integration-content">
                            <p>Connect your Google Search Console for SEO insights.</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.info("Google Search Console integration will be available in the next update")

        # Validate integrations
        changes_made = True  # Always allow proceeding since integrations are coming soon
        has_valid_integrations = True
        validation_message = "✅ Website platform integrations will be available in the next update"

        # Display validation message
        if validation_message:
            if "✅" in validation_message:
                st.success(validation_message)
            else:
                st.warning(validation_message)

        # Navigation buttons
        if render_navigation_buttons(5, 6, changes_made):
            if has_valid_integrations:
                # Store integration settings in session state
                st.session_state['integrations'] = {
                    'coming_soon': {
                        'wordpress': True,
                        'wix': True,
                        'facebook': True,
                        'instagram': True,
                        'google_search_console': True
                    }
                }
                
                # Update progress and move to next step
                st.session_state['current_step'] = 6
                st.rerun()
            else:
                st.error("Please configure at least one integration to continue")

        return {"current_step": 5, "changes_made": changes_made}

    except Exception as e:
        error_msg = f"Error in ALwrity integrations setup: {str(e)}"
        logger.error(f"[render_alwrity_integrations] {error_msg}")
        st.error(error_msg)
        return {"current_step": 5, "error": error_msg} 