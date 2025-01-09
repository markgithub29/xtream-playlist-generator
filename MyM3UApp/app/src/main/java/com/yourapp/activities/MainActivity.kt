package com.yourapp.activities

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.GridLayoutManager
import com.yourapp.R
import com.yourapp.adapters.GroupAdapter
import com.yourapp.models.Group
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Example: Dummy Groups
        val groups = listOf(Group("INDIA"), Group("TELUGU"), Group("SPORTS"))

        recyclerView.layoutManager = GridLayoutManager(this, 2)
        recyclerView.adapter = GroupAdapter(groups) { group ->
            // On Group Click
            val intent = Intent(this, PlayerActivity::class.java)
            intent.putExtra("group_name", group.name)
            startActivity(intent)
        }
    }
}
