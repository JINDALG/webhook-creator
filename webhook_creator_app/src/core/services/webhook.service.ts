import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {
  WEBHOOK_CREATE_API,
  WEBHOOK_DETAIL_API,
  WEBHOOK_LIST_API,
} from '../constants/webhook-api.const';
import { Webhook } from '../models/webhook.model';

@Injectable({
  providedIn: 'root',
})
export class WebhookService {
  constructor(private httpClient: HttpClient) {}

  getWebHooksList(): Observable<Array<Webhook>> {
    return this.httpClient.get<any>(WEBHOOK_LIST_API);
  }

  getWebhookDetails(webhookId: number) {
    return this.httpClient.get(WEBHOOK_DETAIL_API(webhookId));
  }

  createWebHook(data: any) {
    return this.httpClient.post(WEBHOOK_CREATE_API, data);
  }
}
