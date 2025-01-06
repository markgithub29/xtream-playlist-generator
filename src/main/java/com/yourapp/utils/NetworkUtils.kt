package com.yourapp.utils

import okhttp3.OkHttpClient
import okhttp3.Request

object NetworkUtils {

    private val client = OkHttpClient()

    fun fetchM3U(url: String): String {
        val request = Request.Builder().url(url).build()
        client.newCall(request).execute().use { response ->
            return response.body?.string() ?: ""
        }
    }
}
