package com.yourapp.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.yourapp.R
import com.yourapp.adapters.GroupAdapter
import com.yourapp.models.Group
import com.yourapp.utils.M3UParser
import com.yourapp.utils.NetworkUtils
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val recyclerView = findViewById<RecyclerView>(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)

        GlobalScope.launch(Dispatchers.IO) {
            val m3uContent = NetworkUtils.fetchM3U("YOUR_M3U_LINK")
            val groups = M3UParser.parseM3U(m3uContent)

            withContext(Dispatchers.Main) {
                recyclerView.adapter = GroupAdapter(groups)
            }
        }
    }
}
