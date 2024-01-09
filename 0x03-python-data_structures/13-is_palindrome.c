#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add -nodeint - adds a new node at the beggining
 * @head: head of listint_t
 * @n: int to add in listint_t
 * Return: address of new element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 * is_palindrome - identify if a list is palindrome
 * @head: head of listint_t
 * Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed = NULL;
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next !=NULL)
	{
		add_nodeint(&reversed, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
	{
		if (slow->n != reversed->n)
		{
			free_listint(reversed);
			return (0);
		}
		slow = slow->next;
		reversed = reversed->next;
	}
	free_listint(reversed);
	return (1);
}
