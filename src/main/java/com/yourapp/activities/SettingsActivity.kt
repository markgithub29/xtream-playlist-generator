package com.yourapp.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.yourapp.R

class SettingsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)
        // Implement light/dark mode toggle and admin settings
    }
}
