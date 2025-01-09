package com.yourapp.utils

import com.yourapp.models.Channel

object M3UParser {
    fun parseM3U(content: String): List<Channel> {
        // Parse M3U Content
        val channels = mutableListOf<Channel>()
        content.lines().forEach { line ->
            if (line.startsWith("#EXTINF")) {
                val channelName = line.substringAfter(",").trim()
                val url = line.substringAfter("http").trim()
                channels.add(Channel(channelName, url))
            }
        }
        return channels
    }
}
